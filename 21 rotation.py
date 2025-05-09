#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 19:00
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   21 rotation.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 getRotationMatrix2D, warpAffine)
from random import randint, choice


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_ROTATE: str = "Rotate"

    IMAGE: str = "images/emotions/surprise.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Rotate the image with the method of relative size
        rows, cols, _ = image.shape
        ANGLE: int = randint(0, 360)
        CENTER: tuple = (int(cols / 2), int(rows / 2))
        ZOOM: int = choice([0.5, 1, 1.5])
        M = getRotationMatrix2D(CENTER, ANGLE, ZOOM)
        rotate = warpAffine(image, M, (cols, rows))
        imshow(WINDOW_ROTATE, rotate)
        print(f"The image has been rotated to {ANGLE} degrees anticlockwise.")
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
