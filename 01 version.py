#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/4/17 12:27
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   01 version.py
# @Desc     :   

from cv2 import __version__


def main() -> None:
    """ Main Function """
    print(f"OpenCV version: {__version__}")


if __name__ == "__main__":
    main()
