# Devlog 1: Basic Mesh Rendering Pipeline

The next step is to get a very basic rendering pipeline up and running to render our first shape.

## Handing a Shader Program

For this step, we create a class [`pynecraft.shader_program.ShaderProgram`](../source/shader_program.md) that encapsulates the handling of shaders by interacting directly with an OpenGL context provided by moderngl. This class also implements abstractions for reading the shader source code and setting the values of input and uniform variables to the vertex shader.

## Writing the Shaders

Shaders are specialized programs written in a C-like language called GLSL and are used in a graphics pipeline to control various aspects of rendering, such as lighting, texture mapping, and color computations. These programs run on the GPU and are essential for generating the visual effects seen in video games and computer-generated imagery in films.

### Vertex Shader

The vertex shader is the first programmable stage in the graphics pipeline. It processes vertex data. Each vertex's data might include positions, colors, normals, and texture coordinates. This makes it ideal to implement logics like transformations like rotation, scaling, translation, as well as lighting calculations based on vertex normals.

We write a simple and straightforward vertex shader that takes vertices with positions and colors, passes those colors directly through to the fragment shader, and transforms the positions into clip space, preparing them for further processing by the GPU's rasterization stage.

```glsl
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
```

### Fragment Shader

Vertex shaders process each vertex individually and pass their output to the next stage (often a geometry shader or directly to the rasterizer). After rasterization, which turns geometric shapes into a screen-space grid of fragments, the fragment shader runs for each fragment to determine the final pixel color. They determine the color and other attributes of each pixel by processing data passed from the vertex shader. This makes it ideal to implement logics like applying textures to fragments and position-dependent effects like specular highlights, bump mapping, shadows, etc.

We write a very simple fragment shader that takes an RGB color input for each fragment, adds full opacity to it, and outputs the resulting RGBA color.

```glsl
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
```

## A Hierarchy of Meshes

A Mesh is basically a 3D object that is to be rendered in the 3D environment. In order to manage the logic of handling and rendering meshes, we create the abstract base class [`pynecraft.mesh.base.BaseMesh`](../source/mesh/base.md) from which other meshes like [`pynecraft.mesh.QuadMesh`](../source/mesh/quad.md) can be inherited. All we need to define in the inherited mesh classes is the vertex data structure, the input attributes to the vertex shader corresponding to the vertex data structure, and the format of the vertex buffer object.

These Mesh objects can be then put together in a [`pynecraft.scene.Scene`](../source/scene.md) which basically contains a list of meshes and how to render them, along with any additional logic for the update loop of the engine. The `Scene` basically denotes the 3D environment we're rendering and interacting with the in the game world.

!!! note

    The source code of this checkpoint can be found at [PR #2](https://github.com/soumik12345/pynecraft/pull/2). The source code is heavily documented.
