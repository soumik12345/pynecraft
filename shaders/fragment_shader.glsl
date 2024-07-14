// the shader is writter for OpenGL 3.3 core profile
#version 330 core

// output of the fragment shader that will store the
// final color of the fragment (pixel) that is output
// to the framebuffer
layout (location = 0) out vec4 frag_color;

// input variable from the vertex shader
in vec3 color;

void main() {
    // adds an alpha value to the color
    frag_color = vec4(color, 1.0);
}