#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw
from inky.auto import auto
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', type=str, required=True, help="Image to be processed")
args, _ = parser.parse_known_args()
name = args.file

print("""Inky pHAT/wHAT: Logo
# Displays the Inky pHAT/wHAT logo.
""")

# # Get the current path
PATH = os.path.dirname(__file__)

# Set up the Inky display
try:
    inky_display = auto(ask_user=True, verbose=True)
except TypeError:
    raise TypeError("You need to update the Inky library to >= v1.1.0")

try:
    inky_display.set_border(inky_display.BLACK)
except NotImplementedError:
    pass

img = Image.open(os.path.join(PATH, name))
draw = ImageDraw.Draw(img)
inky_display.set_image(img)
inky_display.show()
