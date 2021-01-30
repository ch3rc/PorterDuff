"""
Author:     Cody Hawkins
Class:      CompSci 6420
Date:       1/29/2021
File:       porter-duff.py
Desc:       Provide to images and perform porter/duff operations
            clear, copy, over, in, out, atop, xor
"""

import getopt
import sys
import os
import cv2 as cv
import numpy as np


def help():
    print("\n\t\t-------HELP---------")
    print("porter-duff [image1] [image2] [mask1] [mask2]")
    print("[image1]: source picture")
    print("[image2]: destination picture")
    print("[mask1]: mask of source picture")
    print("[mask2]: mask of destination picture")
    print("If no mask is provided then a mask of non-zero pixels will be created")
    print("If no pictures provided then a square and cross will be drawn and operations will be performed on them")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)

    for o, a in opts:
        if o in ("-h", "--help"):
            help()
        else:
            assert False, "Unhandled Option!"


if __name__=='__main__':
    main()