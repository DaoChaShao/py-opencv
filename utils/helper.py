#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/17 13:39
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :   

from cv2 import (waitKey, destroyWindow,
                 imshow,
                 destroyAllWindows,
                 VideoCapture, CAP_AVFOUNDATION)
from time import perf_counter


def ascii_number_getter(key: str) -> int:
    """ Get the ASCII number of a character

    :param key: The character to get the ASCII number of the key input
    :type key: str
    :return: The ASCII number of the character
    """
    if len(key) == 1:
        return ord(key)
    else:
        raise ValueError("The key should be a single character.")


def image_in_sub_window_displayer(window_name: str, image: any) -> None:
    """ Display an image in a window

    :param window_name: The name of the window
    :type window_name: str
    :param image: The image to display
    :type image: any
    """
    imshow(window_name, image)
    while True:
        if (key := waitKey(100) & 0xFF) == ord("q"):
            print(f"Key {key} pressed, the image window will be closed.")
            destroyWindow(window_name)
            break


def opencv_exit() -> None:
    """ Exit OpenCV

    :return: None
    """
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


class Timer(object):
    """ A simple timer class to measure the elapsed time.

    :param precision: the number of decimal places to round the elapsed time
    :type precision: int
    :param description: the description of the timer
    :type description: str
    :return: None
    """

    def __init__(self, description: str = None, precision: int = 5):
        self._description: str = description
        self._precision: int = precision
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        self._start = perf_counter()
        print(f"{self._description} has been started:")
        print("-" * 50)
        return self

    def __exit__(self, *args):
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        if self._elapsed != 0.0:
            print("-" * 50)
            return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."
        return f"{self._description} has NOT been started."


def cameras_lister(amount: int = 5) -> list:
    """ List the available cameras on the system.

    :param amount: The number of cameras to check
    :type amount: int
    :return: A list of available camera indices
    """
    AVAILABLE: list[int] = []
    for i in range(amount):
        capture = VideoCapture(i, CAP_AVFOUNDATION)
        if capture.isOpened():
            AVAILABLE.append(i)
            capture.release()
    return AVAILABLE
