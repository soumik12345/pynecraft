# Devlog 2: Add a basic first-persor camera and player system

If you look at the rendering of the quad from the previous devlog, you'll notice that although the quad was suppossed to be a square with equal dimensions, its kinda stretched horizontally. This is because we're not taking the aspect ration of the window into account while translating the coordinates of the mesh vertices into OpenGL world coordinates. We're gonna fix this by creating a camera system.

## Camera

We create a [`pynecraft.camera.Camera`](../source/camera.md) class designed to handle the position and orientation of a virtual camers within a 3D game world. It manages the camera's perspective projection and its transformation based on player input or other in-game events. The `Camera` class is initialized using a [`pynecraft.parameters.CameraParameters`](../source/parameters.md) object.

### Field of View

I referred to the article [FOV Calculation: Understanding Field of View in Photography](https://shotkit.com/field-of-view/) By [Teryani Riggs](https://shotkit.com/author/teryani-riggs/) to understand the concept of horizontal and vertical field of view.

|![](https://shotkit.com/wp-content/uploads/2021/12/Focal-length-copy.jpg)|
|---|
|The figure is taken from the aforemention article. The term **angle of view** is not to be confused with the term **field of view**. The angle of view is the angular size of the view cone while the field of view is the maximum area our camera can capture at a given lens focal length of a lens.|

For a virual camera, field of view refers to the angle between the top and bottom of the view frustum. It determines how much of the scene is visible vertically from the camera's perspective. A larger field of view makes more of the scene visible vertically, which can make the game feel more immersive.

The **horizontal field of view** is derived from the vertical field of view using the aspect ratio of the game window. This ensures that the field of view remains consistent and proportionate across different screen sizes and aspect ratios. By adjusting the vertical field of view and the aspect ratio, the horizontal field of view is automatically adjusted to provide a correct and visually pleasing perspective.

From this idea, we can establish the relation between FOV and horizontal FOX as the following:

$$ tan(\frac{FOV_h}{2}) = Aspect Ratio * tan(\frac{FOV_v}{2}) $$

Therefore, horizontal FOV can be expressed as the following

$$ FOV_h = 2 * arctan(Aspect Ratio * tan(\frac{FOV_v}{2})) $$

## First-person Player

If you really think of it, a first-person player is basically a camera with first-person keyboard and mouse controls. Hence we implment the [`pynecraft.player.FirstPersonPlayer`](../source/player.md) class by inheriting from `Camera` and adding keyboard and mouse controls to control the movement and rotation of the camera.

![type:video](./assets/camera.mp4)

!!! note

    The source code of this checkpoint can be found at [PR #3](https://github.com/soumik12345/pynecraft/pull/3). The source code is heavily documented.