import moderngl

from .mesh import QuadMesh


class Scene:
    """A scene that defines a collection of meshes and renders them.

    Args:
        opengl_context (moderngl.Context): The OpenGL context.
        program (moderngl.Program): The shader program used to render the scene.
    """

    def __init__(
        self, opengl_context: moderngl.Context, program: moderngl.Program
    ) -> None:
        self.mesh = QuadMesh(opengl_context=opengl_context, program=program)

    def update(self) -> None:
        pass

    def render(self):
        """Render the scene."""
        self.mesh.render()
