"""
Author:     Cody Hawkins
Class:      CompSci 6420
Date:       1/29/2021
File:       pd_over.py
Desc:       Show src over dest or dest over src
"""
import cv2 as cv
import numpy as np


def over(img_1, img_2, alpha_1, alpha_2, flag):

    if flag:
        # operations for drawn objects
        gray_1 = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
        gray_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

        _, alpha_1 = cv.threshold(gray_1, 0, 255, cv.THRESH_BINARY)
        _, alpha_2 = cv.threshold(gray_2, 0, 255, cv.THRESH_BINARY)

        alpha_1 = cv.merge((alpha_1, alpha_1, alpha_1)) / 255
        alpha_2 = cv.merge((alpha_2, alpha_2, alpha_2)) / 255

        img1_ = img_1 * alpha_1 + img_2 * (1 - alpha_1)
        img2_ = img_2 * alpha_2 + img_1 * (1 - alpha_2)

        output = np.hstack((img1_/255, img2_/255))

    if flag is False:
        # operations for input images/masks
        img_1 = cv.resize(img_1, (640, 480), interpolation=cv.INTER_CUBIC)
        img_2 = cv.resize(img_2, (640, 480), interpolation=cv.INTER_CUBIC)

        if alpha_1 is None and alpha_2 is None:
            # Create masks if none are provided
            lower = np.array([0, 100, 0])

            upper = np.array([150, 255, 100])

            mask = cv.inRange(img_1, lower, upper)

            black = np.zeros_like(img_1)

            black[mask == 0] = 255

            gray_b = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

            _, field = cv.threshold(gray_b, 225, 255, cv.THRESH_BINARY)

            black = black / 255
            field = field / 255

        if alpha_1 is not None and alpha_2 is not None:
            # set masks to known variables
            black = alpha_1 / 255
            field = alpha_2 / 255

        field = cv.merge((field, field, field))

        img1_ = img_1 * black + img_2 * (1 - black)

        img2_ = img_2 * (1 - field) * (1 - black) + img_1 * black

        output = np.hstack((img1_/255, img2_/255))

    return output
