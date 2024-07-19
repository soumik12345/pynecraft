from typing import Tuple

from pydantic import BaseModel


class CameraParameters(BaseModel):
    position: Tuple[float, float, float] = (0, 0, 1)
    yaw: float = -90
    pitch: float = 0
    field_of_view: float = 50.0
    near_plane_of_view_frustum: float = 0.1
    far_plane_of_view_frustum: float = 2000.0
    pitch_max: float = 89


class FirstPersonPlayerParameters(BaseModel):
    player_speed: float = 5e-3
    player_rotation_speed: float = 3e-3
    mouse_sensitivity: float = 2e-3
    camera_parameters: CameraParameters


class EngineParameters(BaseModel):
    window_resolution: Tuple[int, int]
    depth_buffer_size: int
    background_color: Tuple[int, int, int] = (0, 0, 0)
    player_parameters: FirstPersonPlayerParameters
