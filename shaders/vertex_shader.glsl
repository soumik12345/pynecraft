// the shader is writter for OpenGL 3.3 core profile
#version 330 core

// input variables to the vertex shader
layout (location = 0) in vec3 in_position;
layout (location = 1) in vec3 in_color;

// output variables from the vertex shader, passes the
// color data to the fragment shader
out vec3 color;

void main() {
    color = in_color;
    // `gl_Position` is a predefined variable that must
    // be set in every vertex shader
    gl_Position = vec4(in_position, 1.0);
}