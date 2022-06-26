from pathlib import Path
from PIL import Image

dir_images = Path("../_images")
facteur = 3

im = Image.open(dir_images/"rose.png")
t = im.size
t_resized = (round(t[0]/facteur), round(t[1]/facteur))
im.resize(t_resized).show()
