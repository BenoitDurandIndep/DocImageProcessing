from pathlib import Path
from PIL import Image

dir_images = Path("../_images")

im = Image.open(dir_images/"rose.png").convert("RGBA")
logo = Image.open(dir_images/"logo_transp.png").convert("RGBA")


def copyright(image: Image, logo: Image, position: str = "ul", margin: int = 10):
    width, height = image.size
    logo_width, logo_height = logo.size
    coord = {"ul": (0+margin, 0+margin),
             "dl": (0+margin, height-margin-logo_height),
             "ur": (width-margin - logo_width, 0+margin),
             "dr": (width-margin - logo_width, height-margin-logo_height)
             }

    image.paste(logo, coord.get(position), logo)
    image.show()


copyright(image=im, logo=logo, position="dr", margin=20)
