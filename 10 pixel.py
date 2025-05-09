#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 14:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   10 pixel.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows)
from random import randint


def main() -> None:
    """ Main Function """
    WINDOW_NAME: str = "Main"
    namedWindow(WINDOW_NAME, WINDOW_NORMAL)

    IMAGE: str = "images/emotions/1-s-20250418131640.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")

        # Get the width and height of the image loaded
        height, width, _ = image.shape
        print(f"The height of image is {height} and the width is {width}.")
        # Get the pixel value at (0, 0)
        X: int = randint(0, width - 1)
        Y: int = randint(0, height - 1)
        pixel = image[X, Y]
        print(f"The pixel value at ({X}, {Y}) is {pixel}.")

        # Change the pixel value at (X, Y)
        colour: tuple[int, int, int] = (randint(0, 255), randint(0, 255), randint(0, 255))
        print(f"The random pixel value is {colour}.")
        pixel = colour
        print(f"The value of the pixel has been changed {pixel} at ({X}, {Y}).")

        imshow(WINDOW_NAME, image)
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
