from pathlib import Path
from PIL import Image,ImageEnhance
from _image_utils import compare

dir_images = Path("../_images")
im=Image.open(dir_images/"portrait.jpg")

list_images=[]

for i in range(1,10):
    im_filtre=ImageEnhance.Color(im).enhance(i/10)
    list_images.append(im_filtre)

compare(*list_images)
