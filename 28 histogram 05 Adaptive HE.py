#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/26 17:25
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   28 histogram 05 Adaptive HE.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 createCLAHE,
                 calcHist)
from plotly.graph_objects import Figure, Bar
from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_ADA: str = "Adaptive"

    IMAGE: str = "images/emotions/0-s-20250418131750.png"
    image = imread(IMAGE, 0)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Adaptive histogram equalization
        clahe = createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        adaptive = clahe.apply(image)
        print(f"The type of image is {type(adaptive)}")
        print(f"The shape of image is {adaptive.shape}")
        print(f"The dtype of image is {adaptive.dtype}")
        print(f"The pixel size of image is {adaptive.size}")
        imshow(WINDOW_ADA, adaptive)

        # Set the histogram of the adaptive image
        histogram = calcHist([adaptive], [0], None, [256], [0, 256]).flatten()

        # Display the histogram
        fig = Figure()
        fig.add_trace(Bar(
            x=list(range(256)),
            y=histogram,
            name="Histogram",
            marker={"color": "royalblue"},
        ))
        fig.update_layout(
            title="Grayscale Histogram",
            xaxis_title="Pixel Value (0-255)",
            yaxis_title="Frequency",
            template="plotly_white",
        )
        fig.show()
    else:
        print("Failed to load image from path. Please check the path.")

    opencv_exit()


if __name__ == "__main__":
    main()
