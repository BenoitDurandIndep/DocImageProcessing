from pathlib import Path
from PIL import Image, ExifTags
import piexif
from glob import glob
import requests
import shutil


dir_images = Path("../_images/gps")
dir_images_orig = dir_images/"origine"
url = "https://nominatim.openstreetmap.org/reverse.php?format=json"

if not Path.is_dir(dir_images_orig):
    dir_images_orig.mkdir()

for image in glob(f"{str(dir_images)}/*.jpg"):
    exif_dict = piexif.load(image)
    try:
        gps_lat = exif_dict.get("GPS").get(piexif.GPSIFD.GPSLatitude)
        gps_lon = exif_dict.get("GPS").get(piexif.GPSIFD.GPSLongitude)
    except IndexError:
        continue

    lat = gps_lat[0][0]
    lon = gps_lon[0][0]

    req = requests.get(f"{url}&lat={lat}&lon={lon}")
    country = req.json().get("address").get("country")
    #print(f"image:{image} country:{country}")
    dir_country = dir_images_orig/country

    if not Path.is_dir(dir_country):
        dir_country.mkdir()

    shutil.copy(image, dir_country)
