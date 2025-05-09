#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/19 18:30
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   19 zoom - relative size.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 waitKey, destroyAllWindows,
                 resize, INTER_CUBIC)


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_ZOOM: str = "Zoom"

    IMAGE: str = "images/emotions/0-s-20250418131750.png"
    image = imread(IMAGE, 1)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Zoom the image with the method of relative size
        scale: float = 0.5
        zoom = resize(image, None, fx=scale, fy=scale, interpolation=INTER_CUBIC)
        imshow(WINDOW_ZOOM, zoom)
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
