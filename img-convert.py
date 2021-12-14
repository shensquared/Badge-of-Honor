# from inky import InkyPHAT

# inky_display = InkyPHAT("red")
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', type=str, required=True, help="Image to be processed")
args, _ = parser.parse_known_args()
name = args.file

from PIL import Image, ImageFont, ImageDraw

img = Image.open(name)
# img = ImageChops.invert(img)
# Create the palette
# img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))

pal_img = Image.new("P", (1, 1))
pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

# Process the image using the palette
img = img.convert("RGB").quantize(palette=pal_img)
# img.save('ha')
img.show()
img.save('inky-'+name)

width, height = img.size
# print(width, height)
# print(img.format, img.size, img.mode)