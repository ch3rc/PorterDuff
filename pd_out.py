import cv2 as cv
import numpy as np


def out(img_1, img_2, alpha_1, alpha_2, flag):
    if flag:
        gray_1 = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
        gray_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

        _, alpha_1 = cv.threshold(gray_1, 0, 255, cv.THRESH_BINARY)
        _, alpha_2 = cv.threshold(gray_2, 0, 255, cv.THRESH_BINARY)

        alpha_1 = cv.merge((alpha_1, alpha_1, alpha_1))
        alpha_2 = cv.merge((alpha_2, alpha_2, alpha_2))

        alpha_a = (alpha_1/255) * (1-alpha_2/255)
        alpha_b = (alpha_2/255) * (1 - alpha_1/255)

        img1_ = img_1 * alpha_a
        img2_ = img_2 * alpha_b

        output = np.hstack((img1_/255, img2_/255))

    if alpha_1 is None and alpha_2 is None and flag is False:
        img_1 = cv.resize(img_1, (640, 480), interpolation=cv.INTER_CUBIC)
        img_2 = cv.resize(img_2, (640, 480), interpolation=cv.INTER_CUBIC)
        # set upper and lower boundaries for green screen
        lower = np.array([0, 100, 0])

        upper = np.array([150, 255, 100])

        mask = cv.inRange(img_1, lower, upper)

        black = np.zeros_like(img_1)

        black[mask == 0] = 255

        gray_b = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)
        _, field = cv.threshold(gray_b, 225, 255, cv.THRESH_BINARY)

        field = cv.merge((field, field, field))

        a_1 = (black / 255) * (1 - field / 255)
        b_1 = (1 - black / 255) * (1 - field / 255)
        img1_ = img_1 * a_1
        img2_ = img_2 * b_1

        output = np.hstack((img1_/255, img2_/255))


    return output