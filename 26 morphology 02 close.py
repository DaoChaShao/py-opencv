#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/26 14:12
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   26 morphology 02 close.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 morphologyEx, MORPH_CLOSE)
from numpy import ones

from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_CLOSE_WITHOUT_KERNEL: str = "Close without kernel"
    WINDOW_CLOSE_WITH_KERNEL: str = "Close with kernel"

    IMAGE: str = "images/letter-holes.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Transform the image without kernel
        kernel = None
        image_without_kernel = morphologyEx(image, 2, kernel)
        print(f"The type of image is {type(image_without_kernel)}")
        print(f"The shape of image is {image_without_kernel.shape}")
        print(f"The dtype of image is {image_without_kernel.dtype}")
        print(f"The pixel size of image is {image_without_kernel.size}")
        imshow(WINDOW_CLOSE_WITHOUT_KERNEL, image_without_kernel)

        # Transform the image with kernel
        kernel = ones((10, 10), dtype=image.dtype)
        image_with_kernel = morphologyEx(image, MORPH_CLOSE, kernel)
        print(f"The type of image is {type(image_with_kernel)}")
        print(f"The shape of image is {image_with_kernel.shape}")
        print(f"The dtype of image is {image_with_kernel.dtype}")
        print(f"The pixel size of image is {image_with_kernel.size}")
        imshow(WINDOW_CLOSE_WITH_KERNEL, image_with_kernel)
        print("The image has been transformed")
    else:
        print("Failed to load image from path. Please check the path.")

    opencv_exit()


if __name__ == "__main__":
    main()
