import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", required=True,
                    help="path to the image file")
args = vars(parser.parse_args())

image_name = args["path"]

print("Reading image", image_name)