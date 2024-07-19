from typing import Tuple

import pygame

from .camera import Camera
from .parameters import FirstPersonPlayerParameters


class FirstPersonPlayer(Camera):
    """Manages the first-person player's movement and camera control within the 3D game world.

    Args:
        window_resolution (Tuple[float, float]): The resolution of the window.
        player_parameters (FirstPersonPlayerParameters): The parameters of the first-person player.
    """

    def __init__(
        self,
        window_resolution: Tuple[float, float],
        player_parameters: FirstPersonPlayerParameters,
    ) -> None:
        self.player_speed = player_parameters.player_speed
        self.player_rotation_speed = player_parameters.player_rotation_speed
        self.mouse_sensitivity = player_parameters.mouse_sensitivity
        super().__init__(
            window_resolution=window_resolution,
            camera_parameters=player_parameters.camera_parameters,
        )

    def keyboard_control(self, delta_time: float):
        """Handles the keyboard input for controlling the player's movement.

        Args:
            delta_time (float): The time elapsed since the last frame.
        """
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
        """Handles the mouse input for controlling the player's camera orientation."""
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
        """Update the player's movement and camera control using the core game logic.

        Args:
            delta_time (float): The time elapsed since the last frame.
        """
        self.keyboard_control(delta_time=delta_time)
        self.mouse_control()
        super().update()
