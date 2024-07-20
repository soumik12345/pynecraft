from typing import Optional, Tuple

from fire import Fire

from pynecraft.engine import PyneCraftEngine
from pynecraft.parameters import (
    CameraParameters,
    EngineParameters,
    FirstPersonPlayerParameters,
)


def main(
    window_resolution: Tuple[int, int] = (1600, 900),
    depth_buffer_size: int = 24,
    background_color: Optional[Tuple[int, int, int]] = [0, 0, 0],
    player_speed: float = 5e-3,
    player_rotation_speed: float = 3e-3,
    mouse_sensitivity: float = 2e-3,
    position: Tuple[float, float, float] = (0, 0, 1),
    yaw: float = -90,
    pitch: float = 0,
    field_of_view: float = 50.0,
    near_plane_of_view_frustum: float = 0.1,
    far_plane_of_view_frustum: float = 2000.0,
    pitch_max: float = 89,
):
    camera_parameters = CameraParameters(
        position=position,
        yaw=yaw,
        pitch=pitch,
        field_of_view=field_of_view,
        near_plane_of_view_frustum=near_plane_of_view_frustum,
        far_plane_of_view_frustum=far_plane_of_view_frustum,
        pitch_max=pitch_max,
    )
    player_parameters = FirstPersonPlayerParameters(
        player_speed=player_speed,
        player_rotation_speed=player_rotation_speed,
        mouse_sensitivity=mouse_sensitivity,
        camera_parameters=camera_parameters,
    )
    engine_parameters = EngineParameters(
        window_resolution=window_resolution,
        depth_buffer_size=depth_buffer_size,
        background_color=background_color,
        player_parameters=player_parameters,
    )
    engine = PyneCraftEngine(engine_parameters=engine_parameters)
    engine.run()


if __name__ == "__main__":
    Fire(main)
