#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/9 15:43
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   33 hough transform 01 lines.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 Canny,
                 HoughLines, line)
from numpy import pi, sin, cos

from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_EDGES: str = "Edges Detector"
    WINDOW_HOUGH: str = "Hough"

    IMAGE: str = "images/calendar.png"
    image = imread(IMAGE, 0)

    if image is None:
        print("Failed to load image from path. Please check the path.")
    else:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Detect the edges of the image
        # - The thresholds are 50 and 150
        # - The threshold II should be 2 or 3 times bigger than threshold I
        # - The aperture size should be odd numbers, such as 3, 5, 7
        edges = Canny(image, 50, 150, apertureSize=3)
        print(f"The type of image is {type(edges)}")
        print(f"The shape of image is {edges.shape}")
        print(f"The dtype of image is {edges.dtype}")
        print(f"The pixel size of image is {edges.size}")
        imshow(WINDOW_EDGES, edges)

        # Detect the lines of the image with the Hough Transform
        # - The higher of rho, the lower the resolution (accuracy) is.
        lines = HoughLines(edges, 0.8, pi / 180, 150)
        if lines is None:
            print("No lines were found.")
        else:
            for l in lines:
                rho, theta = l[0]
                a = cos(theta)
                b = sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Display the image with the lines
        imshow(WINDOW_HOUGH, image)

    opencv_exit()


if __name__ == "__main__":
    main()
