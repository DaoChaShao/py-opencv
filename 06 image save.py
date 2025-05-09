#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/18 16:20
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   06 image save.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 cvtColor, COLOR_BGR2GRAY,
                 imwrite)

from utils.helper import (image_in_sub_window_displayer,
                          opencv_exit,
                          Timer)


def main() -> None:
    """ Main Function """
    # Set the main window
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)
    print(f"Window {WINDOW_MAIN.upper()} created.")

    # Set the female window and load its image
    IMAGE: str = "images/emotions/surprise.png"
    image = imread(IMAGE)
    if image is not None:
        print(f"The type of image in the {WINDOW_MAIN.upper()} window is {type(image)}")
        print(f"The shape of image in the {WINDOW_MAIN.upper()} window is {image.shape}")
        # Display the image in the window
        imshow(WINDOW_MAIN, image)
        print(f"Image {IMAGE.upper()} displayed in the {WINDOW_MAIN.upper()} window.")
    else:
        print(f"Failed to load image from {IMAGE}. Please check the path.")

    # Convert the image to grayscale
    gray = cvtColor(image, COLOR_BGR2GRAY)

    # Display the grayscale image in the window
    WINDOW_GRAY: str = "Gray"
    image_in_sub_window_displayer(WINDOW_GRAY, gray)

    # Save the grayscale image
    with Timer("Save image") as timer:
        IMAGE_OUTPUT: str = "images/emotions/surprise_gray.png"
        imwrite(IMAGE_OUTPUT, gray)
        print(f"Image {WINDOW_GRAY} saved in {IMAGE_OUTPUT}.")
    print(timer)

    # Display the window and wait indefinitely until the key of ESC is pressed
    opencv_exit()


if __name__ == "__main__":
    main()
