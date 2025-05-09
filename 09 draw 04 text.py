#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 14:35
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   09 draw 04 text.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 putText,
                 FONT_HERSHEY_COMPLEX)
from random import randint


def main() -> None:
    """ Main Function """
    WINDOW_NAME: str = "Main"
    namedWindow(WINDOW_NAME, WINDOW_NORMAL)

    IMAGE: str = "images/emotions/surprise.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of Image is {type(image)}")
        print(f"The shape of Image is {image.shape}")

        # Get the center point of the image
        height, width, _ = image.shape
        print(f"The height of image is {height} and the width is {width}.")
        X: int = int(randint(0, width - 1))
        Y: int = int(randint(0, height - 1))
        print(f"The X coordinate of image center is {X} and Y is {Y}.")
        # Draw a text on the image
        text: str = "Hello World!"
        font: int = FONT_HERSHEY_COMPLEX
        scale: float = 2.0
        colour: tuple[int, int, int] = (0, 255, 0)
        thickness: int = 5
        putText(image, text, (X, Y), font, scale, colour, thickness)

        imshow(WINDOW_NAME, image)
        print(f"Image {IMAGE} displayed in window.")
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
