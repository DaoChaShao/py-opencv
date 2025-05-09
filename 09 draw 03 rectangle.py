#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 14:23
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   09 draw 03 rectangle.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 rectangle)
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

        # Get the width and height of the image loaded
        height, width, _ = image.shape
        print(f"The height of image is {height} and the width is {width}.")
        START: int = randint(0, height - 1)
        END: int = randint(0, width - 1)
        print(f"The height and width of the start point is ({START}, {START})")
        print(f"The height and width of the end point is ({END}, {END})")
        # Draw a rectangle on the image
        colour: tuple[int, int, int] = (0, 255, 0)  # Green color in BGR
        thickness: int = 5
        rectangle(image, (START, START), (END, END), colour, thickness)

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
