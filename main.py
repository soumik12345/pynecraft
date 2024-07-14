from typing import Optional, Tuple

from fire import Fire

from pynecraft.engine import PyneCraftEngine


def main(
    window_resolution: Tuple[int, int] = (1600, 900),
    depth_buffer_size: int = 24,
    background_color: Optional[Tuple[int, int, int]] = [0, 0, 0],
):
    engine = PyneCraftEngine(window_resolution, depth_buffer_size, background_color)
    engine.run()


if __name__ == "__main__":
    Fire(main)
