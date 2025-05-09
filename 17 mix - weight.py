#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 17:47
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   17 mix - weight.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 addWeighted)
from numpy import random
from random import choice, randint


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_NOISE: str = "Noise"
    WINDOW_MIX: str = "Mix"

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

        # Mix the two images
        weight: list[float] = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        alpha: float = choice(weight)
        beta: float = round(1 - alpha, 1)
        # Safe range
        # gamma_for_lightness: int = randint(-255, 255)
        gamma_for_lightness: int = 0
        mix = addWeighted(image, alpha, noise, beta, gamma_for_lightness)
        print(f"The weight of the image is {alpha}.")
        print(f"The weight of the noise is {beta}.")
        print(f"The weight lightness of the mix is {gamma_for_lightness}.")

        imshow(WINDOW_MIX, mix)
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
