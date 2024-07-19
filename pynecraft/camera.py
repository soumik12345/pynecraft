import math

import glm


class Camera:

    def __init__(
        self,
        window_resolution: glm.vec2,
        position,
        yaw,
        pitch,
        field_of_view: float = 50.0,
        near_plane_of_view_frustum: float = 0.1,
        far_plane_of_view_frustum: float = 2000.0,
        pitch_max=89,
    ) -> None:
        self.window_resolution = window_resolution
        self.position = glm.vec3(position)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)
        self.field_of_view = field_of_view
        self.near_plane_of_view_frustum = near_plane_of_view_frustum
        self.far_plane_of_view_frustum = far_plane_of_view_frustum
        self.pitch_max = pitch_max

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
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0.0, 1.0, 0.0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update_view_matrix(self):
        self.view_matrix = glm.lookAt(
            self.position, self.position + self.forward, self.up
        )

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def rotate_pitch(self, vertical_offself):
        self.pitch -= vertical_offself
        self.pitch = glm.clamp(self.pitch, -self.pitch_max, self.pitch_max)

    def rotate_yaw(self, horizontal_offself):
        self.yaw += horizontal_offself

    def move_left(self, velocity):
        self.position -= self.right * velocity

    def move_right(self, velocity):
        self.position += self.right * velocity

    def move_up(self, velocity):
        self.position += self.up * velocity

    def move_down(self, velocity):
        self.position -= self.up * velocity

    def move_forward(self, velocity):
        self.position += self.forward * velocity

    def move_backward(self, velocity):
        self.position -= self.forward * velocity
