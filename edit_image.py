import argparse

import cv2
import imutils
import numpy
from os import path

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", required=True,
                    help="path to the image file")
args = vars(parser.parse_args())

image_name = args["path"]
image_name_root, image_name_extension = path.splitext(image_name)

rotated_name = image_name_root + "_rotated" + image_name_extension
line_name = image_name_root + "_line" + image_name_extension

image = cv2.imread(image_name)
rotated = imutils.rotate(image, 90)
h = image.shape[0]

line_img = cv2.line(image, (300, 0), (300, h), (0, 0, 255), 1)

cv2.imwrite(rotated_name, rotated)
cv2.imwrite(line_name, line_img)

cv2.imshow("Ori", image)
cv2.imshow("Rot", rotated)
cv2.waitKey(0)
