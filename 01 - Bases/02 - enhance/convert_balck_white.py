from pathlib import Path
from PIL import Image, ImageEnhance
from _image_utils import compare
from glob import glob

dir_images = Path("../_images")
dir_images_save = Path("../_images/save")

for image in glob(str(dir_images/"*.jpg")):
    im = Image.open(image)

    im_split = im.split()

    compare(*im_split).save(dir_images_save/Path(image).name)
