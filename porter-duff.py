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
from pd_over import over
from pd_in import In
from pd_out import out
from pd_atop import atop
from pd_xor import xor


def help():
    print("\n\t\t-------HELP---------")
    print("porter-duff [image1] [image2] [mask1] [mask2]")
    print("[image1]: source picture")
    print("[image2]: destination picture")
    print("[mask1]: mask of source picture")
    print("[mask2]: mask of destination picture")
    print("If no mask is provided then a mask of non-zero pixels will be created")
    print("If no pictures provided then a square and cross will be drawn and operations will be performed on them")


def search(filename, directory):
    results = []
    for root, dirs, files in os.walk(directory):
        if filename in files:
            results.append(os.path.join(root, filename))
    return results[0]


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


def clear(img_1, img_2):
    img1_ = np.zeros((480, 640, 3), dtype=img_1.dtype)
    img2_ = np.zeros((480, 640, 3), dtype=img_2.dtype)
    output = np.hstack((img1_, img2_))
    return output


def copy(img_1, img_2):
    img1_ = np.copy(img_1)
    img2_ = np.copy(img_2)
    img1_ = cv.resize(img1_, (640, 480), interpolation=cv.INTER_CUBIC)
    img2_ = cv.resize(img2_, (640, 480), interpolation=cv.INTER_CUBIC)
    output = np.hstack((img1_, img2_))
    return output


def run_operations(img_1, img_2, m_1=None, m_2=None, flag=False):
    img_clear = clear(img_1, img_2)
    img_copy = copy(img_1, img_2)
    img_over = over(img_1, img_2, m_1, m_2, flag)
    img_in = In(img_1, img_2, m_1, m_2, flag)
    img_out = out(img_1, img_2, m_1, m_2, flag)
    img_atop = atop(img_1, img_2, m_1, m_2, flag)
    img_xor = xor(img_1, img_2, m_1, m_2, flag)
    cv.imshow("clear", img_clear)
    cv.waitKey(0)
    cv.imshow("copy", img_copy)
    cv.waitKey(0)
    cv.imshow("img_over", img_over)
    cv.waitKey(0)
    cv.imshow("in", img_in)
    cv.waitKey(0)
    cv.imshow("out", img_out)
    cv.waitKey(0)
    cv.imshow("atop", img_atop)
    cv.waitKey(0)
    cv.imshow("xor", img_xor)
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():

    image_1 = None
    image_2 = None
    mask_1 = None
    mask_2 = None
    flag = False
    path = "C:\\Users\\codyh\\Desktop\\Test Pics"
    path = os.path.abspath(path)
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
        image_1 = search(args[0], path)
        image_2 = search(args[1], path)
        mask_1 = search(args[2], path)
        mask_2 = search(args[3], path)
        run_operations(image_1, image_2, m_1=mask_1, m_2=mask_2, flag=flag)
    elif len(args) == 2:
        print("in here!")
        image_1 = search(args[0], path)
        image_2 = search(args[1], path)
        image_1 = cv.imread(image_1)
        image_2 = cv.imread(image_2)
        run_operations(image_1, image_2, m_1=None, m_2=None, flag=flag)
    elif len(args) == 1:
        print("Too few arguments passed")
    elif len(args) == 0:
        flag = True
        circle, cross = create_objects()
        run_operations(circle, cross, m_1=None, m_2=None, flag=flag)


if __name__ == '__main__':
    main()