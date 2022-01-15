#ifdef GL_ES
precision mediump float;
#endif

#define PI 3.14159265359

uniform vec2 resolution;
uniform vec2 mouse;
uniform float time;


vec3 colorA = vec3(0.149,0.141,0.912);
vec3 colorB = vec3(1.000,0.833,0.224);


void main(){
  vec2 pos = gl_FragCoord.xy/resolution;
  float intensity = step(pos.x,.5);
  // float intensity = pow(pos.x,9.);
  float plot_intensity = plot(pos, intensity);

  vec3 color = vec3(1.-plot_intensity) + plot_intensity*vec3(0.,1.,0.);
  gl_FragColor = vec4(color,1.);
}
