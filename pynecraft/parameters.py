from typing import Tuple

from pydantic import BaseModel


class CameraParameters(BaseModel):
    """Camera parameters.

    Args:
        position (Tuple[float, float, float]): The position of the camera.
        yaw (float): The yaw of the camera in degrees.
        pitch (float): The pitch of the camera in degrees.
        field_of_view (float): The field of view of the camera in degrees.
            This is the extent of the observable world that is seen at any
            given moment by the camera (or the player's eye) in a game.
        near_plane_of_view_frustum (float): The distance of near clipping
            plane of the view frustum from the point of view.
        far_plane_of_view_frustum (float): The distance of far clipping
            plane of the view frustum from the point of view.
        pitch_max (float): The maximum pitch of the camera in degrees.
    """

    position: Tuple[float, float, float] = (0, 0, 1)
    yaw: float = -90
    pitch: float = 0
    field_of_view: float = 50.0
    near_plane_of_view_frustum: float = 0.1
    far_plane_of_view_frustum: float = 2000.0
    pitch_max: float = 89


class FirstPersonPlayerParameters(BaseModel):
    """First person player parameters.

    Args:
        player_speed (float): The speed of the player.
        player_rotation_speed (float): The rotation speed of the player.
        mouse_sensitivity (float): The sensitivity of the mouse control.
        camera_parameters (CameraParameters): The parameters of the camera.
    """

    player_speed: float = 5e-3
    player_rotation_speed: float = 3e-3
    mouse_sensitivity: float = 2e-3
    camera_parameters: CameraParameters


class EngineParameters(BaseModel):
    """PyneCraft engine parameters.

    Args:
        window_resolution (Tuple[int, int]): The resolution of the window
            in pixels.
        depth_buffer_size (int): The size of the depth buffer in bits.
            A larger depth buffer size can improve the visual quality
            of the 3D scene by reducing artifacts such as z-fighting,
            where two surfaces are so close together that the depth buffer
            cannot distinguish which is in front. Common values for depth
            buffer size are `16`, `24`, or `32` bits, with `24` bits being
            a typical choice for balancing performance and precision.
        background_color (Optional[Tuple[int, int, int]], optional): The background
            color of the window.
        player_parameters (FirstPersonPlayerParameters): The parameters of the player.
    """

    window_resolution: Tuple[int, int]
    depth_buffer_size: int
    background_color: Tuple[int, int, int] = (0, 0, 0)
    player_parameters: FirstPersonPlayerParameters
