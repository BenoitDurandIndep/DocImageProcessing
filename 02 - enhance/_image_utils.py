from pathlib import Path
from PIL import Image

dir_images = Path("../_images")

def compare(*args):
    width,height=zip(*(i.size for i in args))

    total_width=sum(width)
    total_height=max(height)

    image_finale=Image.new("RGB",(total_width,total_height))

    offset_x=0
    for img in args:
        image_finale.paste(img,(offset_x,0))
        offset_x+=img.size[0]

    image_finale.show()
    return image_finale

# im1=Image.open(dir_images/"rose.jpg")    
# im2=Image.open(dir_images/"ville.jpg")
# im3=Image.open(dir_images/"portrait.jpg")

# compare(im1,im2,im3)