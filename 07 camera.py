#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/18 16:40
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   07 camera.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 VideoCapture,
                 CAP_AVFOUNDATION,
                 CAP_PROP_AUTOFOCUS, CAP_PROP_BRIGHTNESS, CAP_PROP_CONTRAST,
                 imshow, waitKey,
                 destroyAllWindows)

from utils.helper import cameras_lister


def main() -> None:
    """ Main Function """
    # List the code of the available cameras
    # cameras: list[int] = cameras_lister()
    # print(cameras)

    # Set the main window
    WINDOW_MAIN: str = "main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    # Set the video capture
    capture = VideoCapture(1, CAP_AVFOUNDATION)
    # Set autofocus: 1 for on, 0 for off
    capture.set(CAP_PROP_AUTOFOCUS, 1)
    # Set brightness and contrast
    capture.set(CAP_PROP_BRIGHTNESS, 75)
    capture.set(CAP_PROP_CONTRAST, 50)

    # Display the video
    while True:
        result, frame = capture.read()
        if not result:
            print("Failed to capture video")
            break

        # Display the frame
        imshow(WINDOW_MAIN, frame)

        # Wait for a key press
        if (key := waitKey(100) & 0xFF) == 27:
            break
        elif key != 255:
            print(f"Key {key} pressed.")

    # Release the video capture
    capture.release()
    # Destroy all windows
    destroyAllWindows()


if __name__ == "__main__":
    main()
