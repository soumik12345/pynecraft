from abc import ABC, abstractmethod
from typing import List

import moderngl
import numpy as np


class BaseMesh(ABC):
    """A base class for a mesh object that can be rendered in an OpenGL context.

    Args:
        opengl_context (moderngl.Context): The OpenGL context.
        program (moderngl.Program): The shader program used to render the mesh.
    """

    def __init__(
        self, opengl_context: moderngl.Context, program: moderngl.Program
    ) -> None:
        super().__init__()
        self.opengl_context = opengl_context
        self.program = program
        self.vbo_format: str = None
        self.attributes: List[str] = None
        self.vertex_array_object: moderngl.VertexArray = None

    @abstractmethod
    def get_vertex_data(self) -> np.array:
        """Returns the vertex data for the mesh."""
        pass

    def get_vertex_array_object(self) -> moderngl.VertexArray:
        """Returns a VertexArray object for the mesh.

        Returns:
            moderngl.VertexArray: The VertexArray object.
        """
        vertex_data = self.get_vertex_data()

        # A vertex buffer object is an OpenGL object that stores vertex data
        # such as position, color, texture coordinates, and normals in GPU
        # memory, which is efficient for rendering because it minimizes the
        # data transfer between CPU and GPU.
        vertex_buffer_object = self.opengl_context.buffer(vertex_data)

        # A vertext array object is an OpenGL object that stores the format of
        # the vertex data as well as the method of extracting vertex data from
        # one or more vertex buffer objects. Essentially it stores the parameters
        # to interpret the vertex data structure.
        vertex_array_object = self.opengl_context.vertex_array(
            self.program,
            [(vertex_buffer_object, self.vbo_format, *self.attributes)],
            skip_errors=True,
        )

        return vertex_array_object

    def render(self):
        """Renders the mesh."""
        self.vertex_array_object.render()
