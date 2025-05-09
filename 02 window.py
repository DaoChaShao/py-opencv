#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/17 13:16
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   02 window.py
# @Desc     :   

from cv2 import (namedWindow,
                 WINDOW_NORMAL,
                 waitKey, destroyAllWindows)


def main() -> None:
    """ Main Function """
    WINDOW_NAME: str = "OpenCV Window for Python"
    namedWindow(WINDOW_NAME, WINDOW_NORMAL)
    print(f"Window {WINDOW_NAME.upper()} created.")

    print("Press any key to close the window...")
    # Wait indefinitely until a key is pressed or set a timeout, such as 1000 milliseconds
    waitKey(0)

    # Destroy all windows
    destroyAllWindows()
    print("The window has been closed.")


if __name__ == "__main__":
    main()
