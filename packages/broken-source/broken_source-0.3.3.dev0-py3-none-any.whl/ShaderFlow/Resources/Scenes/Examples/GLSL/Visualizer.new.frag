#define GRID_SIZE 5

vec2 get_star(vec2 seed, vec2 offset) {
    vec2 other = noise22(seed + offset) * 2 * iTime;
    return offset + sin(other)*0.1;
}

vec4 disk() {
    vec2 gluv = iCamera.gluv;
    vec4 color = vec4(0);
    float radius = 0.4;
    int strips = 10;

    if (length(gluv) < radius) {
        float radar;
        radar += 0.10 + 0.004*cos(strips*3*TAU*length(gluv));
        radar *= 0.80 + 0.4*(1 - fract(atan2n(gluv) + 0.2*iTime));
        color.a = smoothstep(radius, 0.95*radius, length(gluv));
        color.rgb = vec3(radar);
        color.rgb *= 0.5 + 1.2*length(gluv + 0.5);
        radar *= color.a;
    } else {
        // gluv = gluv * rotate2deg(90.0);
        float angle = 2*atan2n(gluv);
        vec2 spec = sqrt(texture(iSpectrogram, vec2(0, angle)).xy / 40000);
        float freq = gluv.y<0 ? spec.x:spec.y;
        // freq *= 0.1 + 20*smoothstep(0, 1, angle);

        if (length(gluv) < radius + freq) {
            color.rgb = vec3(1, 1, 1);
            color.a = 1;
        }
    }


    // radar = abs(atan2n(gluv));
    return color;
}

vec4 background() {
    vec2 gluv = iCamera.gluv;
    vec4 color = vec4(vec3(0.2), 1);

    // Build a Blocks GLUV grid with their "chunk id seed"
    vec2 _grid = (stuv2gluv(gluv)) * (GRID_SIZE/2);
    vec2  grid = fract(_grid) - 0.5;
    vec2  seed = floor(_grid);

    vec2 stars[9]; {
        int index = 0;
        for (int ox=-1; ox<2; ox++) {
            for (int oy=-1; oy<2; oy++) {
                stars[index++] = get_star(seed, vec2(ox, 0));
            }
        }
    }

    // Draw lines
    float neuron = 0;

    for (int i=0; i<4; i++) {
        float away = sdLineSegment(grid, stars[4], stars[2*i+1]);
        neuron = max(neuron, smoothstep(0.1, 0.08, away));
    }
    color.rgb += vec3(neuron*0.05);
    // color.rg += grid;
    // color.rgb += abs(seed)/10;
    if (abs(grid.x)>0.98 || abs(grid.y)>0.98) color.rgb = vec3(0.18);

    return color;
}

void main() {
    vec4 color;
    color = blend(color, background());
    color = blend(color, disk());
    fragColor = color;
}
