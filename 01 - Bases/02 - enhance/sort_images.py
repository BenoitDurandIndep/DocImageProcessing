from turtle import width
from PIL import Image
from glob import glob
from shutil import copy
from pathlib import Path

dir_images = Path("..\_images\images")

for image in glob(str(dir_images/"*.jpg")):
    width = Image.open(image).size[0]

    if width < 250:
        dest = dir_images/"small"
    elif width < 500:
        dest = dir_images/"medium"
    elif width < 1000:
        dest = dir_images/"large"
    else:
        dest = dir_images/"extra-large"

    copy(image, dest)
