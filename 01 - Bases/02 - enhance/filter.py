from pathlib import Path
from PIL import Image,ImageEnhance
from _image_utils import compare

dir_images = Path("../_images")

im=Image.open(dir_images/"ville.jpg")
gradient=Image.open(dir_images/"degrade.png")

gradient=gradient.resize(im.size)
images=[]
images.append(im)

for i in range (1,5):
    im_filter=Image.blend(im,gradient,i/10)

    images.append(im_filter)

compare(*images)