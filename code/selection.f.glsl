#ifdef GL_ES
precision mediump float;
out vec4 FragColor;
#endif
uniform int ballID;

void main()
{
#ifdef GL_ES
	FragColor = vec4(float(ballID)/255.0, 0.0, 0.0, 1.0);
#else
	gl_FragColor = vec4(ballID/255.0, 0.0, 0.0, 1.0);
#endif
}
