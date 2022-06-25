from turtle import width
from PIL import Image
from glob import glob
from shutil import copy
from pathlib import Path

rep_images = Path("..\_images\images")

for image in glob(str(rep_images/"*.jpg")):
    width = Image.open(image).size[0]

    if width < 250:
        dest = rep_images/"small"
    elif width < 500:
        dest = rep_images/"medium"
    elif width < 1000:
        dest = rep_images/"large"
    else:
        dest = rep_images/"extra-large"

    copy(image, dest)
