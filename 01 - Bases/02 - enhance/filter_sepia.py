from imaplib import IMAP4_stream
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
from _image_utils import compare

dir_images = Path("../_images")

im = Image.open(dir_images/"noiretblanc.jpg").convert("L")

images = []
images.append(im)
im2 = ImageOps.colorize(im, (132, 84, 129), (240, 176, 113))
images.append(im2)
im3 = ImageEnhance.Contrast(im2).enhance(3)
images.append(im3)
im4 = ImageEnhance.Color(im3).enhance(0.5)
images.append(im4)

compare(*images)
