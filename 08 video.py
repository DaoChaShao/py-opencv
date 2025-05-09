#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/18 17:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   08 video.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 VideoCapture,
                 CAP_PROP_FPS,
                 CAP_PROP_FRAME_COUNT, CAP_PROP_POS_FRAMES,
                 imshow, waitKey,
                 destroyAllWindows)


def main() -> None:
    """ Main Function """
    # Set the main window
    WINDOW_MAIN: str = "main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    # Set the video capture
    VIDEO_PATH: str = "images/emotions/happiness.mp4"
    capture = VideoCapture(VIDEO_PATH)

    # Check if the video file opened successfully
    if not capture.isOpened():
        print(f"Error: Could not open video file {VIDEO_PATH}")
        exit()

    # Get the total frames number
    total = int(capture.get(CAP_PROP_FRAME_COUNT))

    # Get
    fps = capture.get(CAP_PROP_FPS)
    delay = int(1000 / fps)

    # Display the video
    while True:
        result, frame = capture.read()
        if not result:
            print()
            print("Video playback finished.")
            break

        # Display the frame
        imshow(WINDOW_MAIN, frame)

        # Get the current frame number
        current = int(capture.get(CAP_PROP_POS_FRAMES))
        print(f"\rProgress: {current}/{total} ({current / total:.1%})", end="", flush=True)

        # Wait for a key press
        if (key := waitKey(delay) & 0xFF) == 27:
            break
        elif key != 255:
            print(f"Key {key} pressed.")

    # Release the video capture
    capture.release()
    # Destroy all windows
    destroyAllWindows()


if __name__ == "__main__":
    main()
