# PyneCraft

An open-source implementation of a voxel-based game engine similar to MineCraft in Python. The primary purpose of this project is to act as personal hands-on journey to re-learn basic computer graphics and game development concepts.

## Installation and Running

```shell
# clone the repository
git clone https://github.com/soumik12345/pynecraft

# enter into the source directory
cd pynecraft

# install the core packages
pip install -e .[core]
```

<details>
    <summary>The game is run by running <code>main.py</code></summary>

    ```
    NAME
        main.py

    SYNOPSIS
        main.py <flags>

    FLAGS
        -w, --window_resolution=WINDOW_RESOLUTION
            Type: Tuple
            Default: (1600, 900)
        -d, --depth_buffer_size=DEPTH_BUFFER_SIZE
            Type: int
            Default: 24
        -b, --background_color=BACKGROUND_COLOR
            Type: Optional
            Default: [0, 0, 0]
        --player_speed=PLAYER_SPEED
            Type: float
            Default: 0.005
        --player_rotation_speed=PLAYER_ROTATION_SPEED
            Type: float
            Default: 0.003
        -m, --mouse_sensitivity=MOUSE_SENSITIVITY
            Type: float
            Default: 0.002
        --position=POSITION
            Type: Tuple
            Default: (0, 0, 1)
        -y, --yaw=YAW
            Type: float
            Default: -90
        --pitch=PITCH
            Type: float
            Default: 0
        --field_of_view=FIELD_OF_VIEW
            Type: float
            Default: 50.0
        -n, --near_plane_of_view_frustum=NEAR_PLANE_OF_VIEW_FRUSTUM
            Type: float
            Default: 0.1
        --far_plane_of_view_frustum=FAR_PLANE_OF_VIEW_FRUSTUM
            Type: float
            Default: 2000.0
        --pitch_max=PITCH_MAX
            Type: float
            Default: 89
    ```
</details>

## Development Logs

I'll be documenting my journey in the form of development logs:

- [Devlog 0: A Basic Window System](https://geekyrakshit.dev/pynecraft/devlogs/00_window_system/)
- [Devlog 1: Basic Mesh Rendering Pipeline](https://geekyrakshit.dev/pynecraft/devlogs/01_mesh_rendering.md)
- [Devlog 2: Add a basic first-persor camera and player system](https://geekyrakshit.dev/pynecraft/devlogs/02_camera.md)

## Acknowledgements

- [Introduction to OpenGL](https://youtube.com/playlist?list=PLvv0ScY6vfd9zlZkIIqGDeG5TUWswkMox&si=aXUCjrtiuZSUxPwL)
- [Learn OpenGL](https://learnopengl.com/)
- [PyGame Docs](https://www.pygame.org/docs/)
- [Coding Minecraft Live](https://youtube.com/playlist?list=PLGKz7VcwUOnHtTCRomUVTnUy7Ey-Z73Pl&si=D59CmnP8POMyhYP4)
- [Creating MineCraft in C++ and OpenGL](https://youtube.com/playlist?list=PLMZ_9w2XRxiYzEuz4klbm8ZR7BfjueoN2&si=brGRdsRDLK1p62kO)
- [Creating a Voxel Engine (like Minecraft) from Scratch in Python](https://youtu.be/Ab8TOSFfNp4?si=K1mX1cMywiUfzlQ1)