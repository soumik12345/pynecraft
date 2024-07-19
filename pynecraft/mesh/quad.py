import moderngl
import numpy as np

from .base import BaseMesh


class QuadMesh(BaseMesh):
    """A mesh representing a quad in 3D space.

    Args:
        opengl_context (moderngl.Context): The OpenGL context.
        program (moderngl.Program): The shader program used to render the mesh.
    """

    def __init__(
        self, opengl_context: moderngl.Context, program: moderngl.Program
    ) -> None:
        super().__init__(opengl_context, program)
        self.vbo_format = "3f 3f"
        self.attributes = ["in_position", "in_color"]
        self.vertex_array_object = self.get_vertex_array_object()

    def get_vertex_data(self) -> np.array:
        """Returns the vertex data for the mesh.
        
        Returns:
            np.array: The vertex data.
        """
        vertices = [
            (0.5, 0.5, 0.0),
            (-0.5, 0.5, 0.0),
            (-0.5, -0.5, 0.0),
            (0.5, 0.5, 0.0),
            (-0.5, -0.5, 0.0),
            (0.5, -0.5, 0.0),
        ]
        colors = [(0, 1, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1)]
        return np.hstack([vertices, colors], dtype="float32")
