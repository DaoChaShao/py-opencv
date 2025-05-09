#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 16:55
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   13 addition.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 add)
from numpy import random


def main() -> None:
    """ Main Function """
    WINDOW_FEMALE: str = "Main"
    namedWindow(WINDOW_FEMALE, WINDOW_NORMAL)

    WINDOW_NOISE: str = "Noise"
    WINDOW_TOGETHER: str = "Together"

    IMAGE: str = "images/emotions/0-s-20250418131750.png"
    female = imread(IMAGE, 1)

    if female is not None:
        print(f"The type of female is {type(female)}")
        print(f"The shape of female is {female.shape}")
        print(f"The dtype of female is {female.dtype}")
        print(f"The pixel size of female is {female.size}")
        imshow(WINDOW_FEMALE, female)

        # Create a random image with the same shape as the original image
        noise = random.randint(0, 256, female.shape, dtype=female.dtype)
        print(f"The type of noise is {type(noise)}")
        print(f"The shape of noise is {noise.shape}")
        print(f"The dtype of noise is {noise.dtype}")
        print(f"The pixel size of noise is {noise.size}")
        imshow(WINDOW_NOISE, noise)

        # Add the two images together
        together = add(female, noise)

        imshow(WINDOW_TOGETHER, together)
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
