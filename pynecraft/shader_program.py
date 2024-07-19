import os

import moderngl


class ShaderProgram:
    """ShaderProgram encapsulates the handling of shaders by interacting
    directly with an OpenGL context provided by moderngl.

    Args:
        opengl_context (moderngl.Context): The OpenGL context.
        shader_dir (str): The directory containing the vertex and fragment
            shader source code files.
    """

    def __init__(self, opengl_context: moderngl.Context, shader_dir: str) -> None:
        self.opengl_context = opengl_context
        self.program = self.get_program(shader_dir=shader_dir)

    def get_program(self, shader_dir: str) -> moderngl.Program:
        assert os.path.isdir(
            shader_dir
        ), f"Shader directory '{shader_dir}' does not exist."

        with open(os.path.join(shader_dir, "vertex_shader.glsl"), "r") as file:
            vertex_shader_source = file.read()

        with open(os.path.join(shader_dir, "fragment_shader.glsl"), "r") as file:
            fragment_shader_source = file.read()

        return self.opengl_context.program(
            vertex_shader=vertex_shader_source, fragment_shader=fragment_shader_source
        )

    def set_uniforms(self):
        pass

    def update(self):
        pass
