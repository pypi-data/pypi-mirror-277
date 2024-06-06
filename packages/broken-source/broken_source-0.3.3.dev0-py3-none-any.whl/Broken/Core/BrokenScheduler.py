import contextlib
import functools
import inspect
import time
from collections import deque
from threading import Lock
from typing import Any, Callable, Deque, Dict, Iterable, List, Optional, Self

from attr import Factory, define, field

from Broken import BIG_BANG
from Broken.Types import Hertz, Seconds


@define
class BrokenTask:
    """A BrokenScheduler's client dataclass"""

    # # Basic

    task: callable = None
    """Function callable to call every synchronization"""

    args: List[Any] = field(factory=list, repr=False)
    """Method's positional arguments"""

    kwargs: Dict[str, Any] = field(factory=dict, repr=False)
    """Method's keyword arguments"""

    output: Any = field(default=None, repr=False)
    """Method's return value of the last call"""

    context: Any = None
    """Context to use when calling task (with statement)"""

    lock: Lock = None
    """Threading Lock to use when calling task (with statement)"""

    enabled: bool = True
    """Whether to enable this client or not"""

    once: bool = False
    """Client will be removed after next call"""

    # # Synchronization

    frequency: Hertz = 60.0
    """Ideal frequency of task calls"""

    frameskip: bool = True
    """Constant deltatime mode (False) or real deltatime mode (True)"""

    freewheel: bool = False
    """"Rendering" mode, do not sleep on real time, exact virtual frametimes"""

    precise: bool = False
    """Use precise time sleeping for near-perfect frametimes"""

    # # Timing
    started: Seconds = Factory(lambda: time.bang_counter())
    """Time when client was started (initializes $now+started, value in now() seconds)"""

    next_call: Seconds = None
    """Next time to call task (initializes $now+next_call, value in now() seconds)"""

    last_call: Seconds = None
    """Last time task was called (initializes $now+last_call, value in now() seconds)"""

    # # Flags
    _time:     bool    = False
    _dt:       bool    = False

    def __attrs_post_init__(self):
        signature = inspect.signature(self.task)
        self._dt   = ("dt"   in signature.parameters)
        self._time = ("time" in signature.parameters)

        # Assign idealistic values for decoupled
        if self.freewheel: self.started = BIG_BANG
        self.last_call = (self.last_call or self.started)
        self.next_call = (self.next_call or self.started)

        # Note: We could use numpy.float128 for the most frametime precision on the above..
        #       .. But the Client code is smart enough to auto adjust itself to sync

    # # Useful properties

    @property
    def fps(self) -> Hertz:
        return self.frequency

    @fps.setter
    def fps(self, value: Hertz):
        self.frequency = value

    @property
    def period(self) -> Seconds:
        return 1/self.frequency

    @period.setter
    def period(self, value: Seconds):
        self.frequency = 1/value

    @property
    def tag_delete(self) -> bool:
        return self.once and (not self.enabled)

    @property
    def tag_alive(self) -> bool:
        return not self.tag_delete

    # # Sorting

    def __lt__(self, other: Self) -> bool:
        return self.next_call < other.next_call

    def __gt__(self, other: Self) -> bool:
        return self.next_call > other.next_call

    # # Implementation

    def next(self, block: bool=True) -> Self:

        # Time to wait for next call if block
        # - Next call at 110 seconds, now=100, wait=10
        # - Positive means to wait, negative we are behind
        wait = max(0, (self.next_call - time.bang_counter()))

        if self.freewheel:
            pass
        elif block:
            if self.precise:
                time.precise_sleep(wait)
            else:
                time.sleep(wait)
        elif wait > 0:
            return None

        # The assumed instant the code below will run instantly
        now = self.next_call if self.freewheel else time.bang_counter()
        if self._dt:   self.kwargs["dt"]   = (now - self.last_call)
        if self._time: self.kwargs["time"] = (now - self.started)

        # Enter or not the given context, call task with args and kwargs
        with (self.lock or contextlib.nullcontext()):
            with (self.context or contextlib.nullcontext()):
                self.output = self.task(*self.args, **self.kwargs)

        # Fixme: This is a better way to do it, but on decoupled it's not "dt perfect"
        # self.next_call = self.period * (math.floor(now/self.period) + 1)

        # Update future and past states
        self.last_call = now
        while self.next_call <= now:
            self.next_call += self.period

        # (Disabled && Once) clients gets deleted
        self.enabled = not self.once

        return self

@define
class BrokenScheduler:
    clients: Deque[BrokenTask] = Factory(deque)

    def add_task(self, client: BrokenTask) -> BrokenTask:
        """Adds a client to the manager with immediate next call"""
        self.clients.append(client)
        return client

    def new(self, task: Callable, *a, **k) -> BrokenTask:
        """Wraps around BrokenVsync for convenience"""
        return self.add_task(BrokenTask(task=task, *a, **k))

    def once(self, task: Callable, *a, **k) -> BrokenTask:
        """Wraps around BrokenVsync for convenience"""
        return self.add_task(BrokenTask(task=task, *a, **k, once=True))

    def partial(self, task: Callable, *a, **k) -> BrokenTask:
        """Wraps around BrokenVsync for convenience"""
        return self.once(task=functools.partial(task=task, *a, **k))

    # # Filtering

    @property
    def enabled_tasks(self) -> Iterable[BrokenTask]:
        """Returns a list of enabled clients"""
        for client in self.clients:
            if client.enabled:
                yield client

    @property
    def next_task(self) -> Optional[BrokenTask]:
        """Returns the next client to be called"""
        return min(self.enabled_tasks)

    def _sanitize(self) -> None:
        """Removes not enabled 'once' clients"""
        self.clients = list(filter(lambda client: client.tag_alive, self.clients))

    # # Actions

    def next(self, block=True) -> Optional[BrokenTask]:
        try:
            if (client := self.next_task):
                return client.next(block=block)
        finally:
            self._sanitize()

    def all_once(self) -> None:
        """Calls all 'once' clients. Useful for @partial calls on the main thread"""
        for client in self.clients:
            if client.once:
                client.next()
        self._sanitize()

    # # Block-free next

    __work__: bool = False

    def smart_next(self) -> Optional[BrokenTask]:
        # Note: Proof of concept. The frametime Ticking might be enough for ShaderFlow

        # Too close to the next known call, call blocking
        if abs(time.bang_counter() - self.next_task.next_call) < 0.005:
            return self.next(block=True)

        # By chance any "recently added" client was added
        if (call := self.next(block=False)):
            self.__work__ = True
            return call

        # Next iteration, wait for work but don't spin lock
        if not self.__work__:
            time.sleep(0.001)

        # Flag that there was not work done
        self.__work__ = False
