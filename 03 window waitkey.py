#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/17 13:27
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   03 window waitkey.py
# @Desc     :

from cv2 import (namedWindow,
                 WINDOW_NORMAL,
                 waitKey, destroyAllWindows)

from utils.helper import ascii_number_getter


def main() -> None:
    """ Main Function """
    WINDOW_NAME: str = "OpenCV Window for Python"
    namedWindow(WINDOW_NAME, WINDOW_NORMAL)
    print(f"Window {WINDOW_NAME.upper()} created.")

    # Print the ASCII number of the key input
    print(ascii_number_getter("q"))

    # Wait indefinitely until the key of ESC is pressed
    print("Press 'ESC' to close the window...")
    # Method I
    # while True:
    #     key: int = waitKey(100) & 0xFF
    #     if key == 27:
    #         print("ESC key pressed.")
    #         break
    #     elif key != 255:
    #         print(f"Key {key} pressed.")
    # Method II
    while True:
        if (key := waitKey(100) & 0xFF) == 27:
            print("ESC key pressed.")
            break
        elif key != 255:
            print(f"Key {key} pressed.")

    # Destroy all windows
    destroyAllWindows()
    print("The window has been closed.")


if __name__ == "__main__":
    main()
