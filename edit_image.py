import argparse

import cv2
import imutils
import numpy
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", required=True,
                        help="path to the image file")
    parser.add_argument("-option", choices=['rotate', 'line', 'bw', 'mask'], required=True,
                        help="Option for image(rotate/line/bw/mask)")
    args = vars(parser.parse_args())

    image_name = args["path"]
    option = args["option"]

    if not os.path.exists(image_name):
        print("Oops, unable to find image", image_name)
        return
    image_name_root, image_name_extension = os.path.splitext(image_name)
    ori = cv2.imread(image_name)

    new_image = None
    name_suffix = ""
    print("Press 's' to save newly created image, after highlighting the image window. Press any other key to exit.")
    if option == "rotate":
        new_image, name_suffix = rotate(ori)
    elif option == "line":
        draw_line(ori, 100)
    elif option == "bw":
        new_image, name_suffix = draw_bw(ori)
    elif option == "mask":
        new_image, name_suffix = draw_mask(ori)

    k = cv2.waitKey(0) & 0xFF  # 0XFF needed for 64 bit machines
    if k == ord('s'):
        new_name = image_name_root + name_suffix + image_name_extension
        print("Saving", new_name)
        cv2.imwrite(new_name, new_image)
    else:
        print("Exiting without saving the new image.")

    cv2.destroyAllWindows()
    cv2.waitKey(1)


def rotate(image):
    print("Rotating image ...")
    rotated = imutils.rotate(image, 90)
    cv2.imshow("Rotated", rotated)
    return rotated, "_rotated"


def draw_line(image, x):
    print("Drawing a line on image ...")
    line = image
    line[:, x] = [0, 0, 255]
    cv2.imshow("Lined", line)
    return line, "_lined"


def draw_bw(image):
    print("Drawing BW image ...")
    bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Black and white", bw)
    return bw, "_bw"


def draw_mask(image):
    image_with_mask = image.copy()
    print("Add a mask to the image ...")
    change_color_pixels = image[:, :, 0] < 20
    image_with_mask[change_color_pixels] = [0, 255, 0]
    cv2.imshow("Image with mask", image_with_mask)
    return image_with_mask, "_mask"


if __name__ == "__main__":
    main()
