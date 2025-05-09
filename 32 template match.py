#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/27 13:16
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   32 template match.py
# @Desc     :
import cv2
from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 bitwise_and,
                 matchTemplate, TM_CCORR, TM_CCOEFF_NORMED,
                 normalize, NORM_MINMAX,
                 minMaxLoc,
                 rectangle)
from numpy import zeros

from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_FACE: str = "Face"
    namedWindow(WINDOW_FACE, WINDOW_NORMAL)

    WINDOW_FACES: str = "Faces"
    WINDOW_MATCH: str = "Match"
    WINDOW_IDENTITY: str = "Identity"

    FACE: str = "images/emotions/0-s-20250418131750.png"
    face = imread(FACE)

    FACES: str = "images/emotions/surprise.png"
    faces = imread(FACES)

    if face is not None:
        print(f"The type of image is {type(face)}")
        print(f"The shape of image is {face.shape}")
        print(f"The dtype of image is {face.dtype}")
        print(f"The pixel size of image is {face.size}")
        imshow(WINDOW_FACE, face)

        face_height, face_width, _ = face.shape

        # Set the image of faces
        if faces is not None:
            print(f"The type of image is {type(faces)}")
            print(f"The shape of image is {faces.shape}")
            print(f"The dtype of image is {faces.dtype}")
            print(f"The pixel size of image is {faces.size}")
            imshow(WINDOW_FACES, faces)

            # Set face match
            match = matchTemplate(faces, face, TM_CCOEFF_NORMED)
            print(f"The type of image is {type(match)}")
            print(f"The shape of image is {match.shape}")
            print(f"The dtype of image is {match.dtype}")
            print(f"The pixel size of image is {match.size}")
            normalize(match, match, 0, 255, NORM_MINMAX)
            match = match.astype("uint8")
            imshow(WINDOW_MATCH, match)

            # Method I
            # min_val, max_val, min_loc, max_loc = minMaxLoc(match)
            # top_left = max_loc
            # bottom_right = (top_left[0] + face_width, top_left[1] + face_height)

            # Method I
            _, _, _, max_loc = minMaxLoc(match)
            bottom_right = (max_loc[0] + face_width, max_loc[1] + face_height)

            colour: tuple[int, int, int] = (0, 255, 0)
            thickness: int = 2
            rectangle(faces, max_loc, bottom_right, colour, thickness)
            imshow(WINDOW_IDENTITY, faces)
    else:
        print("Failed to load image from path. Please check the path.")

    opencv_exit()


if __name__ == "__main__":
    main()
