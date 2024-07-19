import glm
import pygame

from .camera import Camera


class FirstPersonPlayer(Camera):

    def __init__(
        self,
        window_resolution: glm.vec2,
        position,
        yaw,
        pitch,
        player_speed: float = 5e-3,
        player_rotation_speed: float = 3e-3,
        player_position: glm.vec3 = glm.vec3(0, 0, 1),
        field_of_view: float = 50,
        near_plane_of_view_frustum: float = 0.1,
        far_plane_of_view_frustum: float = 2000,
        pitch_max: float = 89,
        mouse_sensitivity: float = 2e-3,
    ) -> None:
        self.player_speed = player_speed
        self.player_rotation_speed = player_rotation_speed
        self.player_position = player_position
        self.mouse_sensitivity = mouse_sensitivity
        super().__init__(
            window_resolution,
            position,
            yaw,
            pitch,
            field_of_view,
            near_plane_of_view_frustum,
            far_plane_of_view_frustum,
            pitch_max,
        )

    def keyboard_control(self, delta_time: float):
        key_state = pygame.key.get_pressed()
        velocity = self.player_speed * delta_time
        if key_state[pygame.K_w]:
            self.move_forward(velocity)
        if key_state[pygame.K_s]:
            self.move_backward(velocity)
        if key_state[pygame.K_a]:
            self.move_left(velocity)
        if key_state[pygame.K_d]:
            self.move_right(velocity)
        if key_state[pygame.K_q]:
            self.move_up(velocity)
        if key_state[pygame.K_e]:
            self.move_down(velocity)

    def mouse_control(self):
        mouse_change_horizontal, mouse_change_vertical = pygame.mouse.get_rel()
        if mouse_change_horizontal:
            self.rotate_yaw(
                horizontal_offset=mouse_change_horizontal * self.mouse_sensitivity
            )
        if mouse_change_vertical:
            self.rotate_pitch(
                vertical_offset=mouse_change_vertical * self.mouse_sensitivity
            )

    def update(self, delta_time: float):
        self.keyboard_control(delta_time=delta_time)
        self.mouse_control()
        super().update()
