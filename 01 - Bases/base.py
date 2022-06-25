from PIL import Image
from pathlib import Path

dir_images = Path("../_images")

# im = Image.new("RGB", (1920, 1080), "red")
# im.show()

im = Image.open(dir_images/"homme.png")
im_png = Image.new("RGB", im.size, "red")
im_png.paste(im, im)
im_png.show()

# im.split()[3].show()
