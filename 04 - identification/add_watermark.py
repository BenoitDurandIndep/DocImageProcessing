from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

dir_images = Path("../_images")

im = Image.open(dir_images/"ville.jpg")
font_path = dir_images/"Roboto-Black.ttf"


def copyright(image: Image, text: str, opacity: float = 1.0, rotation: int = 30):
    image = image.convert("RGBA")
    im_size = image.size
    texte_image = Image.new("RGBA", im_size, (255, 255, 255, 0))

    fontsize = 1
    font = ImageFont.truetype(str(font_path), fontsize)

    while font.getsize(text)[0] < im_size[0]:
        fontsize += 1
        font = ImageFont.truetype(str(font_path), fontsize)

    text_height = font.getsize(text)[1]
    pos = (0, (im_size[1]/2)-(text_height/2))

    draw = ImageDraw.Draw(texte_image)
    draw.text(xy=pos, text=text, fill=(
        255, 255, 255, round(opacity*255)), font=font)

    texte_image = texte_image.rotate(rotation)

    return Image.alpha_composite(image, texte_image)


copyright(image=im, text="BDUR", opacity=0.5, rotation=20).show()
