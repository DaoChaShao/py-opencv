#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 17:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   16 division.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 divide)
from numpy import random


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_NOISE: str = "Noise"
    WINDOW_DIVIDE: str = "Divide"

    IMAGE: str = "images/emotions/0-s-20250418131750.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Create a random image with the same shape as the original image
        noise = random.randint(0, 256, image.shape, dtype=image.dtype)
        print(f"The type of noise is {type(noise)}")
        print(f"The shape of noise is {noise.shape}")
        print(f"The dtype of noise is {noise.dtype}")
        print(f"The pixel size of noise is {noise.size}")
        imshow(WINDOW_NOISE, noise)

        # Divide the two images
        divided = divide(image, noise)

        imshow(WINDOW_DIVIDE, divided)
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
