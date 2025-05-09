#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 14:12
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   09 draw 02 circle.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 circle)


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
        X: int = int(width // 2)
        Y: int = int(height // 2)
        print(f"The X coordinate of image center is {X} and Y is {Y}.")
        # Draw a circle on the image
        radius: int = 50
        colour: tuple[int, int, int] = (0, 255, 0)
        thickness: int = 5
        circle(image, (X, Y), radius, colour, thickness)

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
