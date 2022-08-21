import os
import sys
from PIL import Image

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def divide_until_reached_number(current_num, desired_num):
    while current_num > desired_num:
        current_num = current_num / 2
    return current_num

input_image = input("Choose image to distort: ")
distort_axis = input("Which axis to distort the image on: ").lower()

if distort_axis not in ["x", "y"]:
    sys.exit("Invalid axis input.")

im = Image.open(f"{ROOT_DIR}\\Documents\\{input_image}")
if distort_axis == "x":
    if im.width > 2400:
        new_width = divide_until_reached_number(im.width, 2400)
        resized = im.resize((int((new_width * 50) / 2), im.height))
    elif im.width > 1200:
        resized = im.resize((int((im.width * 25) / 4), im.height))
    elif im.width > 400 :
        resized = im.resize((int((im.width * 50) / 2), im.height))
    else:
        resized = im.resize((im.width * 100, im.height))
elif distort_axis == "y":
    if im.height > 2400:
        new_height = divide_until_reached_number(im.height, 2400)
        resized = im.resize((im.width, int((new_height * 100) / 2)))
    elif im.height > 1200:
        resized = im.resize((im.width, int((im.height * 25) / 4)))
    elif im.height > 400 :
        resized = im.resize((im.width, int((im.height * 50) / 2)))
    else:
        resized = im.resize((im.width, im.height * 100))

resized.save(f"{ROOT_DIR}\\Documents\\{input_image.split('.', 1)[0]}_distorted.png", "png")
print(f"Distortion complete! \nSize Before: X: {im.width} Y: {im.height} \nSize After: X: {resized.width} Y: {resized.height}")