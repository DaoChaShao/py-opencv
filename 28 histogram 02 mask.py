#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/26 16:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   28 histogram 02 mask.py
# @Desc     :   

from cv2 import (namedWindow, WINDOW_NORMAL,
                 imread, imshow,
                 bitwise_and,
                 calcHist)
from numpy import zeros
from plotly.graph_objects import Figure, Bar

from utils.helper import opencv_exit


def main() -> None:
    """ Main Function """
    WINDOW_MAIN: str = "Main"
    namedWindow(WINDOW_MAIN, WINDOW_NORMAL)

    WINDOW_MASK: str = "Mask"
    WINDOW_TOGETHER: str = "Together"

    IMAGE: str = "images/emotions/0-s-20250418131750.png"
    image = imread(IMAGE, 0)

    if image is not None:
        print(f"The type of image is {type(image)}")
        print(f"The shape of image is {image.shape}")
        print(f"The dtype of image is {image.dtype}")
        print(f"The pixel size of image is {image.size}")
        imshow(WINDOW_MAIN, image)

        # Create a mask
        mask = zeros(image.shape, dtype=image.dtype)
        print(f"The type of image is {type(mask)}")
        print(f"The shape of image is {mask.shape}")
        print(f"The dtype of image is {mask.dtype}")
        print(f"The pixel size of image is {mask.size}")
        mask[70:320, 90:260] = 255
        imshow(WINDOW_MASK, mask)

        # Put the mask on the image
        together = bitwise_and(image, mask)
        print(f"The type of image is {type(together)}")
        print(f"The shape of image is {together.shape}")
        print(f"The dtype of image is {together.dtype}")
        print(f"The pixel size of image is {together.size}")
        imshow(WINDOW_TOGETHER, together)

        # Check the histogram of the together image
        histogram = calcHist([together], [0], mask, [256], [0, 256]).flatten()

        # Display the histogram
        fig = Figure()
        fig.add_trace(Bar(
            x=list(range(256)),
            y=histogram,
            name="Gray Histogram",
            marker={"color": "royalblue"},
        ))
        fig.update_layout(
            title="Grayscale Histogram",
            xaxis_title="Pixel Value (0-255)",
            yaxis_title="Frequency",
            template="plotly_white",
        )
        fig.show()
        print("The image has been transformed")
    else:
        print("Failed to load image from path. Please check the path.")

    opencv_exit()


if __name__ == "__main__":
    main()
