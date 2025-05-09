#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/18 15:32
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   04 image load 02 single.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread)

from utils.helper import (image_in_sub_window_displayer,
                          opencv_exit)


def main() -> None:
    """ Main Function """
    # Set the main window
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)
    print(f"Window {WINDOW_MAIN.upper()} created.")

    # Set the female window and load its image
    IMAGE_FEMALE: str = "images/emotions/0-s-20250418131725.png"
    image_female = imread(IMAGE_FEMALE)
    if image_female is not None:
        print(f"The type of image in the {WINDOW_MAIN.upper()} window is {type(image_female)}")
        print(f"The shape of image in the {WINDOW_MAIN.upper()} window is {image_female.shape}")
        # Display the image in the window
        print(f"Image {IMAGE_FEMALE.upper()} displayed in the {WINDOW_MAIN.upper()} window.")
        image_in_sub_window_displayer(WINDOW_MAIN, image_female)
    else:
        print(f"Failed to load image from {IMAGE_FEMALE}. Please check the path.")

    # Display the window and wait indefinitely until the key of ESC is pressed
    opencv_exit()


if __name__ == "__main__":
    main()
