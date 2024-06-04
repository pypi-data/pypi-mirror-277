import cv2
import numpy as np


def read_image(path: str,):
    image = cv2.imread(path)
    return image


def crop_image(image, points=(), kernal_size=(32, 32)):
    if not points:
        cropped_image = []
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh1_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernal_size)
        dilation_image = cv2.dilate(thresh1_image, rect_kernel, iterations=1)
        contours, _ = cv2.findContours(dilation_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cropped_image = image[y:y+h, x:x+w]
        return cropped_image
    else:
        x, y, w, h = points
        cropped_image = image[y:y+h, x:x+w]
        return cropped_image
