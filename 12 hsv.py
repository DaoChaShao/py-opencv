#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 16:41
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   12 hsv.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 cvtColor, COLOR_BGR2HSV)


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_HSV: str = "HSV"

    IMAGE = "images/emotions/surprise.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")

        imshow(WINDOW_MAIN, image)

        # Convert the BGR image to HSV
        hsv = cvtColor(image, COLOR_BGR2HSV)
        print(f"The type of image is {type(hsv)}")
        print(f"The shape of image is {hsv.shape}")
        print(f"The dtype of image is {hsv.dtype}")
        print(f"The pixel size of image is {hsv.size}")

        imshow(WINDOW_HSV, hsv)
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
