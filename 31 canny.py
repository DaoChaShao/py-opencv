#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/27 13:00
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   31 canny.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 Canny)

from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_CANNY: str = "Canny"

    IMAGE: str = "images/emotions/0-s-20250418131725.png"
    image = imread(IMAGE, 0)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Display the edge of the image with canny method
        canny = Canny(image, 0, 100)
        imshow(WINDOW_CANNY, canny)
    else:
        print("Failed to load image from path. Please check the path.")

    opencv_exit()


if __name__ == "__main__":
    main()
