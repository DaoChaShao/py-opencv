#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 16:10
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   11 channels.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 split, merge)
from numpy import zeros_like
from random import randint, choice


def main() -> None:
    """ Main Function """
    WINDOW_NAME: str = "Main"
    namedWindow(WINDOW_NAME, WINDOW_NORMAL)

    WINDOW_B_SINGLE: str = "Single Blue"
    WINDOW_G_SINGLE: str = "Single Green"
    WINDOW_R_SINGLE: str = "Single Red"
    WINDOW_B_MULTIPLE: str = "Multiple Blue"
    WINDOW_G_MULTIPLE: str = "Multiple Green"
    WINDOW_R_MULTIPLE: str = "Multiple Red"
    WINDOW_MERGE: str = "Merge"

    IMAGE: str = "images/emotions/1-s-20250418131640.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")

        imshow(WINDOW_NAME, image)

        # Split the pixel value into BGR channels
        B, G, R = split(image)
        print(f"The pixel value in B is {B.shape}.")
        print(f"The pixel value in G is {G.shape}.")
        print(f"The pixel value in R is {R.shape}.")

        # Create empty arrays like the channel of B, G or R
        zeros = zeros_like(choice((B, G, R)))

        # Create colour image with zeros
        image_B = merge((B, zeros, zeros))
        image_G = merge((zeros, G, zeros))
        image_R = merge((zeros, zeros, R))

        # Display the BGR channels in separate windows
        imshow(WINDOW_B_SINGLE, B)
        imshow(WINDOW_G_SINGLE, G)
        imshow(WINDOW_R_SINGLE, R)
        imshow(WINDOW_B_MULTIPLE, image_B)
        imshow(WINDOW_G_MULTIPLE, image_G)
        imshow(WINDOW_R_MULTIPLE, image_R)

        # Merge the channels back into a single image
        merged_image = merge((B, G, R))
        imshow(WINDOW_MERGE, merged_image)
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
