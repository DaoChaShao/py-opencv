#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/9 16:28
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   33 hough transform 02 circle.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 cvtColor, COLOR_BGR2GRAY,
                 medianBlur,
                 HoughCircles, HOUGH_GRADIENT, circle)

from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_BLUR: str = "Blur"
    WINDOW_HOUGH: str = "Hough"

    IMAGE: str = "images/stars.png"
    image = imread(IMAGE)
    gray = cvtColor(image, COLOR_BGR2GRAY)

    if image is None:
        print("Failed to load image from path. Please check the path.")
    else:
        print(f"The type of image is {type(gray)}")
        print(f"The shape of image is {gray.shape}")
        print(f"The dtype of image is {gray.dtype}")
        print(f"The pixel size of image is {gray.size}")
        imshow(WINDOW_MAIN, gray)

        # Filter the noise of the image with media blur
        blur = medianBlur(gray, 5)
        imshow(WINDOW_BLUR, blur)

        # Detect the circles of the image with the Hough Transform
        stars = HoughCircles(
            blur,
            HOUGH_GRADIENT,
            1.2,  # The accuracy of the centre location
            100,  # min distance between circles
            param1=100,  # max threshold of the Canny-edge detector
            param2=50,  # += threshold
            minRadius=60,  # min radius of the circle
            maxRadius=130,  # max radius of the circle
        )
        if stars is None:
            print("No circles were found.")
        else:
            for index in stars[0, :]:
                center = (int(index[0]), int(index[1]))
                radius = int(index[2])
                # Draw the circles
                circle(image, center, radius, (0, 255, 0), 2)
                # Draw the centres of the circles
                circle(image, center, 2, (0, 0, 255), -1)

        imshow(WINDOW_HOUGH, image)

    opencv_exit()


if __name__ == "__main__":
    main()
