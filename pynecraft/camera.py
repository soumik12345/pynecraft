import math
from typing import Tuple

import glm

from .parameters import CameraParameters


class Camera:
    """A camera class designed to handle the position and orientation of a
    virtual camers within a 3D game world. It manages the camera's perspective
    projection and its transformation based on player input or other in-game
    events. 
    
    Args:
        window_resolution (Tuple[float, float]): The resolution of the window.
        camera_parameters (CameraParameters): The parameters of the camera.
    """

    def __init__(
        self,
        window_resolution: Tuple[float, float],
        camera_parameters: CameraParameters,
    ) -> None:
        self.window_resolution = glm.vec2(window_resolution)
        self.position = glm.vec3(camera_parameters.position)
        self.yaw = glm.radians(camera_parameters.yaw)
        self.pitch = glm.radians(camera_parameters.pitch)
        self.field_of_view = camera_parameters.field_of_view
        self.near_plane_of_view_frustum = camera_parameters.near_plane_of_view_frustum
        self.far_plane_of_view_frustum = camera_parameters.far_plane_of_view_frustum
        self.pitch_max = camera_parameters.pitch_max

        self.aspect_ratio = self.window_resolution.x / self.window_resolution.y
        self.vertical_field_of_view = glm.radians(self.field_of_view)
        self.horizontal_field_of_view = 2 * math.atan(
            math.tan(self.vertical_field_of_view / 2) * self.aspect_ratio
        )

        self.up = glm.vec3(0.0, 1.0, 0.0)
        self.right = glm.vec3(1.0, 0.0, 0.0)
        self.forward = glm.vec3(0.0, 0.0, -1.0)

        self.projection_matrix = glm.perspective(
            self.vertical_field_of_view,
            self.aspect_ratio,
            self.near_plane_of_view_frustum,
            self.far_plane_of_view_frustum,
        )
        self.view_matrix = glm.mat4()

    def update_vectors(self):
        """Update the camera vectors."""
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0.0, 1.0, 0.0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update_view_matrix(self):
        """Update the view matrix."""
        self.view_matrix = glm.lookAt(
            self.position, self.position + self.forward, self.up
        )

    def update(self):
        """Update the camera vectors and view matrix based on the controls."""
        self.update_vectors()
        self.update_view_matrix()

    def rotate_pitch(self, vertical_offset):
        """Rotate the camera pitch."""
        self.pitch -= vertical_offset
        self.pitch = glm.clamp(self.pitch, -self.pitch_max, self.pitch_max)

    def rotate_yaw(self, horizontal_offset):
        """Rotate the camera yaw."""
        self.yaw += horizontal_offset

    def move_left(self, velocity):
        """Move the camera left."""
        self.position -= self.right * velocity

    def move_right(self, velocity):
        """Move the camera right."""
        self.position += self.right * velocity

    def move_up(self, velocity):
        """Move the camera up."""
        self.position += self.up * velocity

    def move_down(self, velocity):
        """Move the camera down."""
        self.position -= self.up * velocity

    def move_forward(self, velocity):
        """Move the camera forward."""
        self.position += self.forward * velocity

    def move_backward(self, velocity):
        """Move the camera backward."""
        self.position -= self.forward * velocity
