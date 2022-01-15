#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 resolution;
uniform vec2 mouse;
uniform float time;

// Plot a line on Y using a value between 0.0-1.0
float plot(vec2 st, float pct){
  return  smoothstep( pct-0.02, pct, st.y) -
          smoothstep( pct, pct+0.02, st.y);
}


void main() {
  vec2 fpos = gl_FragCoord.xy/resolution;

  float intensity_r = (sin(fpos.x*time*50.)+1.)/2.*(sin(fpos.y*10.*time)+1.)/2.;
  float intensity_g = (sin(fpos.x*time)+1.)/2.*(sin(fpos.y*10.*9./16.*time)+1.)/2.;
  float intensity_b = (sin(fpos.x*time*100.)+1.)/2.*(sin(fpos.y*10.*time)+1.)/2.;

  vec3 bg_color = vec3(intensity_r, intensity_g, intensity_b);

  // Plot a line
  // float plot_f = plot(fpos, y);
  // color = (1.0-plot_f)*bg_intensity+plot_f*vec3(0.0,1.0,0.0);

	gl_FragColor = vec4(bg_color,1.0);
}
