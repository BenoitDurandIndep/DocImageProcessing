from pathlib import Path
from PIL import Image
from glob import glob

dir_images = Path("../_images")
dir_images_save = Path("../_images/save")
suffix_img = ".jpg"


def image_thumbnail(im: Image, name: str, ratio: int = 10, suffix: str = ".jpg") -> bool:
    success = False
    im_new = im.copy()
    size = im_new.size
    new_size = (round(size[0]/ratio), round(size[1]/ratio))

    new_suffix = f"-{new_size[0]}x{new_size[1]}{suffix}"

    name_new = name.replace(".jpg", new_suffix)

    im_new.thumbnail(new_size)
    im_new.save(dir_images_save/name_new)
    success = True

    return success


for image in glob(str(dir_images/"*.jpg")):
    im = Image.open(image)
    name_base = Path(image).name
    for ratio in (2, 3, 5, 10):
        image_thumbnail(im, name_base, ratio, suffix_img)
