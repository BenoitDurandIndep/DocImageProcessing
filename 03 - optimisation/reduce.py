from pathlib import Path
from PIL import Image

dir_images = Path("../_images")
facteur = 3

im = Image.open(dir_images/"rose.png")
im.thumbnail((250,250))
im.save(dir_images/"rose-small.png")