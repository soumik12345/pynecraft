import sys
from typing import Optional, Tuple

import moderngl
import pygame


class PyneCraftEngine:
    """The main class of the PyneCraft engine. It is responsible for creating the window, setting up the OpenGL context,
    and running the main loop of the engine. The main loop of the engine is responsible for updating the game state,
    rendering, and handling events.

    Args:
        window_resolution (Tuple[int, int]): The resolution of the window in pixels.
        depth_buffer_size (int): The size of the depth buffer in bits. A larger depth buffer size can improve the
            visual quality of the 3D scene by reducing artifacts such as z-fighting, where two surfaces are so close
            together that the depth buffer cannot distinguish which is in front. Common values for depth buffer size
            are `16`, `24`, or `32` bits, with `24` bits being a typical choice for balancing performance and precision.
        background_color (Optional[Tuple[int, int, int]], optional): The background color of the window.
    """

    def __init__(
        self,
        window_resolution: Tuple[int, int],
        depth_buffer_size: int,
        background_color: Optional[Tuple[int, int, int]] = [0, 0, 0],
    ) -> None:
        self.window_resolution = window_resolution
        self.depth_buffer_size = depth_buffer_size
        self.background_color = background_color

        pygame.init()
        self.set_opengl_attributes()

        # Create the display surface
        pygame.display.set_mode(
            self.window_resolution, flags=pygame.DOUBLEBUF | pygame.OPENGL
        )

        # Create the opengl context
        self.opengl_context = moderngl.create_context()

        # Enable specific OpenGL capabilities for the rendering context.
        # `moderngl.DEPTH_TEST` enables depth testing which ensures that pixels
        # closer to the camera obscure those further away, maintaining the
        # proper visual order of objects.
        # `moderngl.CULL_FACE` enables face culling which is a technique for
        # improving rendering performance by not drawing faces of polygons that
        # are not visible to the camera. Typically, this involves not rendering
        # the back faces of objects, assuming the front faces are sufficient to
        # represent the visible geometry.
        # `moderngl.BLEND` enables blending which is the process of combining the
        # color of a source pixel with the color of a destination pixel based on
        # their alpha values. It is essential for rendering transparent and
        # semi-transparent objects correctly.
        self.opengl_context.enable(
            moderngl.DEPTH_TEST | moderngl.CULL_FACE | moderngl.BLEND
        )

        # Set the garbage collection mode of the OpenGL context to "auto".
        # This enables the OpenGL context to automatically manages the deletion of
        # OpenGL objects (like buffers, textures, and shaders) that are no longer
        # in use. This helps prevent memory leaks and ensures that resources are
        # freed up when they are no longer needed.
        self.opengl_context.gc_mode = "auto"

        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_engine_running = True

    def set_opengl_attributes(self) -> None:
        """Set the values of several attributes for the OpenGL context before creating the display surface."""
        # Set the version of the OpenGL context to 3.3
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)

        # Set the subset of the OpenGL API to be used is the core profile.
        # The core profile includes only the modern, streamlined parts of
        # OpenGL, removing deprecated functions and features.
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
        )

        # Set the size of the depth buffer in bits. The depth buffer is used
        # to handle depth information to determine which objects are in front
        # of others in a 3D scene by keeping track of the depth of each pixel.
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, self.depth_buffer_size)

    def update(self) -> None:
        """Update the game state using the core game logic."""
        self.delta_time = self.clock.tick()
        self.time = pygame.time.get_ticks() * 1e-3
        pygame.display.set_caption(f"PyneCraft | FPS: {self.clock.get_fps()}")

    def render(self) -> None:
        """Render the game state to the screen."""
        self.opengl_context.clear(*self.background_color)
        pygame.display.flip()

    def handle_events(self) -> None:
        """Handle events such as user input and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                self.is_engine_running = False

    def run(self) -> None:
        """Run the main loop of the engine, which updates the game state, renders the game, and handles events."""
        while self.is_engine_running:
            self.update()
            self.render()
            self.handle_events()
        pygame.quit()
        sys.exit()
