from pathlib import Path
from PIL import Image

dir_images = Path("../_images")

im=Image.open(dir_images/"rose.jpg")
#im.transpose(Image.ROTATE_90).show()
im.rotate(45,expand=True,fillcolor="green").show()