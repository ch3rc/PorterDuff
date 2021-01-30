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


def create_objects():
    ###################################################################
    # Create Circle                                                   #
    ###################################################################
    # 640x480 3 channel of zeros
    img_1 = np.zeros((480, 640, 3), dtype=np.uint8)

    # Find center point of image
    center_radius = (img_1.shape[1] // 2, img_1.shape[0] // 2)

    # Set radius of circle
    radius = 150

    # Make circle blue (BGR)
    color = (255, 0, 0)

    # Fill circle in blue
    thickness = -1

    # Create circle and fill array of zeros
    circle = cv.circle(img_1, center_radius, radius, color, thickness)

    ##################################################################
    # Create cross                                                   #
    ##################################################################
    # 640x480 3 channel of zeros
    img_2 = np.zeros((480, 640, 3), dtype=np.uint8)

    # Find top left point for 96x512 rectangle
    start_point_1 = (img_2.shape[1]//2 - 512//2, img_2.shape[0]//2 - 96//2)

    # Find bottom right for 96x512 rectangle
    end_point_1 = (img_2.shape[1]//2 + 512//2, img_2.shape[0]//2 + 96//2)

    # Find top left point for 128x384 rectangle
    start_point_2 = (img_2.shape[1]//2 - 128//2, img_2.shape[0]//2 - 384//2)

    # Find bottom right point for 128x384 rectangle
    end_point_2 = (img_2.shape[1]//2 + 128//2, img_2.shape[0]//2 + 384//2)

    # Red rectangle (BGR)
    rec_color = (0, 0, 255)

    # Fill zeros array with rectangles
    rectangle = cv.rectangle(img_2, start_point_1, end_point_1, rec_color, thickness)
    rectangle = cv.rectangle(rectangle, start_point_2, end_point_2, rec_color, thickness)

    return circle, rectangle


def clear(img):
    output = np.zeros(img.shape, dtype=img.dtype)
    return output


def copy(img):
    output = np.copy(img)
    return output



def run_operations(img_1, img_2, m_1=None, m_2=None):
    pass


def main():

    image_1 = None
    image_2 = None
    mask_1 = None
    mask_2 = None

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

    if len(args) > 4:
        print("Too many arguments provided")
    elif len(args) == 4:
        image_1 = args[0]
        image_2 = args[1]
        mask_1 = args[2]
        mask_2 = args[3]
        run_operations(image_1, image_2, m_1=mask_1, m_2=mask_2)
    elif len(args) == 3:
        image_1 = args[0]
        image_2 = args[1]
        mask_1 = args[2]
        run_operations(image_1, image_2, m_1=mask_1, m_2=None)
    elif len(args) == 2:
        image_1 = args[0]
        image_2 = args[1]
        run_operations(image_1, image_2, m_1=None, m_2=None)
    elif len(args) == 1:
        print("Too few arguments passed")
    else:
        circle, cross = create_objects()
        run_operations(circle, cross, m_1=None, m_2=None)


if __name__=='__main__':
    main()