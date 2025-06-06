#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/23 17:57
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   22 transform 01 affine.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 getAffineTransform, warpAffine)
from numpy import float32


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_TRANSFORM: str = "Transform"

    IMAGE: str = "images/emotions/surprise.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Transform the image with the method of relative size
        height, width, _ = image.shape
        src_points = float32([(0, 0), (width - 1, 0), (0, height - 1)])
        dst_points = float32([(0, 0), (width - 1, 0), (int(width / 2), height - 1)])
        M = getAffineTransform(src_points, dst_points)
        transform = warpAffine(image, M, (width, height))
        imshow(WINDOW_TRANSFORM, transform)
        print("The image has been transformed")
    else:
        print(f"Failed to load image from {IMAGE}. Please check the path.")

    while True:
        if (key := waitKey(100) & 0xFF) == 27:
            print("ESC key pressed.")
            break
        elif key != 255:
            print(f"Key {key} pressed.")

    destroyAllWindows()
    print("Done.")


if __name__ == "__main__":
    main()
