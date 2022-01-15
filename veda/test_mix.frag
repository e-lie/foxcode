#ifdef GL_ES
precision mediump float;
#endif

#define PI 3.14159265359

uniform vec2 resolution;
// uniform vec2 mouse;
// uniform float time;

vec3 colorA = vec3(0.149,0.141,0.912);
vec3 colorB = vec3(1.000,0.833,0.224);

float plot (vec2 st, float pct){
  return  smoothstep( pct - 0.01, pct, st.y) -
          smoothstep( pct, pct + 0.01, st.y);
}

void main() {
    vec2 st = gl_FragCoord.xy/resolution.xy;
    vec3 color = vec3(0.0);

    vec3 pct;

    pct.r = sin(st.x*PI-1.)/2.+.5;
    pct.g = smoothstep(0.0,1.0, st.x);
    pct.b = pow(st.x,0.5);

    color = mix(colorA, colorB, pct);

    // Plot transition lines for each channel
    color = mix(color,vec3(1.0,0.0,0.0),plot(st,pct.r));
    color = mix(color,vec3(0.0,1.0,0.0),plot(st,pct.g));
    color = mix(color,vec3(0.0,0.0,1.0),plot(st,pct.b));

    gl_FragColor = vec4(color,1.0);
}
