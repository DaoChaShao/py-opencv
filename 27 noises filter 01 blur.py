#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/26 14:43
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   27 noises filter 01 blur.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 blur)

from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_BLUR: str = "Blur"

    IMAGE: str = "images/noises-salt-and-paper.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Transform the image
        kernel_size: int = 5
        image_blur = blur(image, (kernel_size, kernel_size))
        print(f"The type of image is {type(image_blur)}")
        print(f"The shape of image is {image_blur.shape}")
        print(f"The dtype of image is {image_blur.dtype}")
        print(f"The pixel size of image is {image_blur.size}")
        imshow(WINDOW_BLUR, image_blur)
        print("The image has been transformed")
    else:
        print("Failed to load image from path. Please check the path.")

    opencv_exit()


if __name__ == "__main__":
    main()
