#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/18 12:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   04 image load 01 main & sub.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 waitKey, destroyAllWindows,
                 imread, imshow)

from utils.helper import image_in_sub_window_displayer


def main() -> None:
    """ Main Function """
    # Set a window
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)
    print(f"Window {WINDOW_MAIN.upper()} created.")

    # Load an image
    IMAGE_MAIN: str = "images/emotions/surprise.png"
    image_main = imread(IMAGE_MAIN, 1)
    if image_main is not None:
        print(f"The type of Image is {type(image_main)}")
        print(f"The shape of Image is {image_main.shape}")
        # Display the image in the window
        imshow(WINDOW_MAIN, image_main)
        print(f"Image {IMAGE_MAIN} displayed in window.")
    else:
        print(f"Failed to load image from {IMAGE_MAIN}. Please check the path.")

    # Load another image
    WINDOW_MAN: str = "Man"
    IMAGE_MAN: str = "images/emotions/1-s-20250418131640.png"
    image_man = imread(IMAGE_MAN)
    if image_man is not None:
        print(f"The type of Image is {type(image_man)}")
        print(f"The shape of Image is {image_man.shape}")
        # Display the image in the window
        image_in_sub_window_displayer(WINDOW_MAN, image_man)
    else:
        print(f"Failed to load image from {IMAGE_MAIN}. Please check the path.")

    # Display the window and wait indefinitely until the key of ESC is pressed
    print("Press 'ESC' to close the all windows...")
    while True:
        if (key := waitKey(100) & 0xFF) == 27:
            print("ESC key pressed.")
            break
        elif key != 255:
            print(f"Key {key} pressed.")

    # Destroy all windows
    destroyAllWindows()
    print("The all window has been closed.")


if __name__ == "__main__":
    main()
