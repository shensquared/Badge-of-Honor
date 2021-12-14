#!/usr/bin/env python3

import os
from PIL import Image, ImageDraw, ImageFont
from font_intuitive import Intuitive
from inky.auto import auto

from github import Github


# print("""Inky pHAT/wHAT: Logo

# Displays the Inky pHAT/wHAT logo.

# """)

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

# Pick the correct logo image to show depending on display resolution/colour

if inky_display.resolution in ((212, 104), (250, 122)):
    if inky_display.resolution == (250, 122):
        if inky_display.colour == 'black':
            img = Image.open(os.path.join(PATH, "inky-drake.png"))
        else:
            img = Image.open(os.path.join(PATH, "inky-drake.png"))

    else:
        if inky_display.colour == 'black':
            img = Image.open(os.path.join(PATH, "phat/resources/InkypHAT-212x104-bw.png"))
        else:
            img = Image.open(os.path.join(PATH, "phat/resources/InkypHAT-212x104.png"))

elif inky_display.resolution in ((400, 300), ):
    if inky_display.colour == 'black':
        img = Image.open(os.path.join(PATH, "what/resources/InkywHAT-400x300-bw.png"))
    else:
        img = Image.open(os.path.join(PATH, "what/resources/InkywHAT-400x300.png"))

elif inky_display.resolution in ((600, 448), ):
    img = Image.open(os.path.join(PATH, "what/resources/InkywHAT-400x300.png"))
    img = img.resize(inky_display.resolution)



draw = ImageDraw.Draw(img)

# Display the logo image
scale_size=1.5
intuitive_font = ImageFont.truetype(Intuitive, size = int(22 * scale_size))
y_top = int(122 * (5.0 / 10.0))
y_bottom = y_top + int(122 * (4.0 / 10.0))



try:
    g = Github()
    repo = g.get_repo("RobotLocomotion/drake")
    stars=str(repo.stargazers_count)
    forks =str(repo.forks_count)

    # pixel location of the star count texts
    star_x = int(40)
    star_y = int(8)
    draw.text((star_x, star_y), stars ,inky_display.BLACK,font=intuitive_font)



    # pixel location of the fork count texts
    fork_x = int(40)
    fork_y = int(50)
    draw.text((fork_x, fork_y), forks,inky_display.BLACK,font=intuitive_font)
    img.save('inky-drake-placeholder.png')
except:
    img = Image.open(os.path.join(PATH, "inky-Wifi.png"))
inky_display.set_image(img)
inky_display.show()