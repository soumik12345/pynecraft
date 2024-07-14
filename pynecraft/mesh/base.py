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
        pass

    def get_vertex_array_object(self) -> moderngl.VertexArray:
        vertex_data = self.get_vertex_data()
        vertex_buffer_object = self.opengl_context.buffer(vertex_data)
        vertex_array_object = self.opengl_context.vertex_array(
            self.program,
            [(vertex_buffer_object, self.vbo_format, *self.attributes)],
            skip_errors=True,
        )
        return vertex_array_object

    def render(self):
        self.vertex_array_object.render()
