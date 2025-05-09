#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/24 13:27
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   23 pyramid 01 up.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 pyrUp)

from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_UP: str = "Up for pixel increase with double size"

    IMAGE: str = "images/emotions/surprise.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Transform the image with the method of relative size
        up = pyrUp(image)
        print(f"The type of image is {type(up)}")
        print(f"The shape of image is {up.shape}")
        print(f"The dtype of image is {up.dtype}")
        print(f"The pixel size of image is {up.size}")
        imshow(WINDOW_UP, up)
        print("The image has been transformed")
    else:
        print("Failed to load image from path. Please check the path.")

    opencv_exit()


if __name__ == "__main__":
    main()
