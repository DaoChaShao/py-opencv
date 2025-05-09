#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/26 22:03
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   29 sobel 02 schaar.py
# @Desc     :   More details

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 Sobel, CV_16S,
                 convertScaleAbs, addWeighted)

from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_SCHAAR: str = "Schaar"

    IMAGE: str = "images/emotions/0-s-20250418131750.png"
    image = imread(IMAGE, 0)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        x = Sobel(image, CV_16S, 1, 0, ksize=1)
        y = Sobel(image, CV_16S, 0, 1, ksize=-1)
        absX = convertScaleAbs(x)
        absY = convertScaleAbs(y)
        schaar = addWeighted(absX, 0.5, absY, 0.5, 0)
        imshow(WINDOW_SCHAAR, schaar)
        print("The edge detection algorithm is done.")
    else:
        print("Failed to load image from path. Please check the path.")

    opencv_exit()


if __name__ == "__main__":
    main()
