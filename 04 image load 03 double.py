#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/18 15:35
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   04 image load 03 double.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 waitKey, destroyAllWindows,
                 imread, imshow,
                 destroyWindow)


def main() -> None:
    """ Main Function """
    # Set the windows, such as female and male
    WINDOW_FEMALE: str = "Female"
    WINDOW_MALE: str = "Man"
    namedWindow(WINDOW_FEMALE, WINDOW_NORMAL)
    namedWindow(WINDOW_MALE, WINDOW_NORMAL)

    # Load the image of female in its window
    IMAGE_FEMALE: str = "images/emotions/0-s-20250418131725.png"
    image_female = imread(IMAGE_FEMALE)
    if image_female is not None:
        # Display the image in the window
        imshow(WINDOW_FEMALE, image_female)
    else:
        print(f"Failed to load image from {IMAGE_FEMALE}. Please check the path.")

    # Load the image of male in its window
    IMAGE_MALE: str = "images/emotions/1-s-20250418131640.png"
    image_man = imread(IMAGE_MALE)
    if image_man is not None:
        # Display the image in the window
        imshow(WINDOW_MALE, image_man)
    else:
        print(f"Failed to load image from {IMAGE_FEMALE}. Please check the path.")

    # Display the windows and wait indefinitely until the key of ESC is pressed
    while True:
        if (key := waitKey(100) & 0xFF) == 27:
            print("ESC key pressed.")
            break
        elif key == ord("f"):
            print(f"Key {key} pressed, the {WINDOW_FEMALE} window will be closed.")
            destroyWindow(WINDOW_FEMALE)
        elif key == ord("m"):
            print(f"Key {key} pressed, the {WINDOW_MALE} window will be closed.")
            destroyWindow(WINDOW_MALE)
        elif key != 255:
            print(f"Key {key} pressed.")

    # Destroy all windows
    destroyAllWindows()
    print("The all window has been closed.")


if __name__ == "__main__":
    main()
