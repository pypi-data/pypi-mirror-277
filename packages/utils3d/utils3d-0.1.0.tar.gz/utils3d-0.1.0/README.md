# utils3d

This Python package provides a collection of utilities for working with 3D data!

## Installation

```bash
$ pip install utils3d
```

## Usage

`utils3d` can be used to perform various actions on your 3d data. One of them is converting the 3D point cloud data into a 2D depth image and that can be achieved as follows:
```python
from utils3d.pctodepthimage import pctodepthimage

path = "pointclouds/um_000000.pcd" # path to your point cloud file
extrinsics = [] # 3x4 numpy array containing the extrinsic parameters (dummy available in tests/test_utils3d.py)
intrinsics = [] # 3x3 numpy array containing the ixtrinsic parameters (dummy available in tests/test_utils3d.py)
height = 512 # height of your depth image
width = 1382 # width of your depth image
scaling_factor = 0.15 # scaling factor manipulates the intensity of the pixels of your image

depth_image = pctodepthimage(path, extrinsics, intrinsics, height, width, scaling_factor)
depth_image.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`utils3d` was created by Kalash Jain. It is licensed under the terms of the MIT license.

## Credits

`utils3d` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
