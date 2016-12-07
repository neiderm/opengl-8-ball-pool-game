OpenGL-8-ball-pool-game
=======================

An interacting billiard game using modern OpenGL API.

[Project Page](http://zhongyn.github.io/opengl-8-ball-pool-game/)

![alt text](https://github.com/zhongyn/opengl-8-ball-pool-game/blob/gh-pages/images/per_fragment.png)


Update 7-Dec-2016 by G. Neidermeier:

I made a few changes to get this program built and working on my present system.
It is running on (X)Ubuntu 16.04 inside Virtual Box.

Here are some of the dependencies you may need to install:
 apt-get install libglew-dev freeglut3-dev libglm-dev libsoil-dev


First error I ran into running the program:

 textures file[0]:BallCue.jpg
 poolgame.v.glsl:0:1(10): error: GLSL 1.50 is not supported. Supported versions are: 1.10, 1.20, 1.30, 1.00 ES, and 3.00 ES

Running glxinfo to confirming supported glsl level:

 OpenGL version string: 3.0 Mesa 11.2.0
 OpenGL shading language version string: 1.30

Shader program is apparently not compatible with GLSL 1.3 (try changing to "#version 130\n" in shader_utils.cpp):

 poolgame.v.glsl:0:25(18): error: no matching function for call to `inverse(mat4)'; candidates are:
 0:25(8): error: no matching function for call to `transpose(error)'; candidates are:

Probably could patch up the shader to make compatible with 1.30, but looking in shader_utils.cpp, appears possible the programs were intended to be compatible with GL|ES. Checking my system with glxinfo:

    Max GLES1 profile version: 1.1
    Max GLES[23] profile version: 3.0

... and es2_info:

 EGL_CLIENT_APIS: OpenGL OpenGL_ES OpenGL_ES2 OpenGL_ES3 
 GL_VERSION: OpenGL ES 3.0 Mesa 11.2.0

A conditional compile to use GL|ES compatible shader is already present in shader_utils.cpp, so give that a try by defining the macro with '-DGL_ES_VERSION_2_0' (GLSL 1.00 ES should be selected using `#version 100'). However, the shader still gives several errors with GLSL 1.00 ES:

 poolgame.v.glsl:0:4(1): error: `in' qualifier in declaration of `v_coord' only valid for function parameters in GLSL 1.10
 0:5(1): error: `in' qualifier in declaration of `v_normal' only valid for function parameters in GLSL 1.10
 0:6(1): error: `in' qualifier in declaration of `v_texcoord' only valid for function parameters in GLSL 1.10
 0:14(1): error: `out' qualifier in declaration of `fN' only valid for function parameters in GLSL 1.10
 0:15(1): error: `out' qualifier in declaration of `fE' only valid for function parameters in GLSL 1.10
 0:16(1): error: `out' qualifier in declaration of `fL' only valid for function parameters in GLSL 1.10
 0:18(1): error: `out' qualifier in declaration of `texcoord' only valid for function parameters in GLSL 1.10
 0:26(18): error: no matching function for call to `inverse(mat4)'; candidates are:
 0:26(8): error: no matching function for call to `transpose(error)'; candidates are:

By now, I am starting to learn some of the distinction between OpenGL ES 2.0 / GLSL 1.00  and OpenGL ES 3.0 / GLSL 3.0! For example, In GLSL 3.00 the 'in' qualifier is used to designate the variables that were formerly referred to as 'attributes', 'varying' becomes 'out'. So rebuilding with "#version 300 es\n" seems to clear some things up, but there are still a few errors out of the fragment shader:

 poolgame.f.glsl:0:4(1): error: No precision specified in this scope for type `vec4'
 0:5(1): error: No precision specified in this scope for type `vec4'
 <snip>
 0:38(2): error: `gl_FragColor' undeclared
 0:38(2): error: value of type vec4 cannot be assigned to variable of type error

Still a few snags compiling the shaders for GL|ES. The special output variable 'gl_FragColor' has been eliminated, and shader output variables are created simply by declaring them with the 'out' qualifier. Thanks to a few helpful hints found over at Beuc's Blog ("http://blog.beuc.net/posts/OpenGL_ES_2.0_using_Android_NDK/") - GL|ES requires float precision hints. Also learned that OpenGL ES 2.0 implementations are required to have a GL_ES macro predefined in the shaders so I was able to remove the '#define GLES2' and so:

 selection.f.glsl:0:7(2): error: `gl_FragColor' undeclared
 0:7(22): error: could not implicitly convert operands to arithmetic operator

The 'convert operands' error is fixed by applying a cast i.e. 'float(ballID)'. With that the billiard balls demo is working on my machine, and the balls will move around when you run the mouse pointer into them!
