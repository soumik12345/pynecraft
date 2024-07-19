# Devlog 0: A Basic Window System

The first step to build an open-source python implementation of a MineCraft-like engine or any game for that matter is to create a Window system that simply shows a blank screen. We do this by createing the `PyneCraftEngine` class that is responsible for creating the window, setting up the OpenGL context, and running the main loop of the engine. The main loop of the engine is responsible for updating the game state, rendering, and handling events.

The source code of this checkpoint can be found at [PR #1](https://github.com/soumik12345/pynecraft/pull/1). The source code is heavily documented.
