from pathlib import Path
from PIL import Image, ExifTags
import piexif
from pprint import pprint

dir_images = Path("../_images")
path_img = str(dir_images/"ville.jpg")

im = Image.open(path_img)


exif = piexif.load(path_img)
exif_bytes = piexif.dump(exif)
pprint(exif)

im.save(dir_images/"ville_upd.jpg", exif=exif_bytes)
