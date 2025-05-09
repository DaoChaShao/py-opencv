#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 18:53
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   20 move.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 warpAffine)
from numpy import float32
from random import randint


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_MOVE: str = "Move"

    IMAGE: str = "images/emotions/0-s-20250418131750.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Move the image with the method of relative size
        rows, cols, _ = image.shape
        X: int = randint(0, cols - 1)
        Y: int = randint(0, rows - 1)
        M = float32([[1, 0, X], [0, 1, Y]])
        move = warpAffine(image, M, (cols, rows))
        imshow(WINDOW_MOVE, move)
        print(f"The image has been moved to {X} at X and {Y} at Y.")
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
