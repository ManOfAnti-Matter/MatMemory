from PIL import Image
import os, sys


def resize_image(image, maxsize):
    r1 = image.width/maxsize[0] # width ratio
    r2 = image.height/maxsize[1] # height ratio
    ratio = max(r1, r2)
    newsize = (int(image.width/ratio), int(image.height/ratio))
    image = image.resize(newsize, Image.LANCZOS)
    return image


path = ".\\Cards"
dirs = os.listdir(path)
for item in dirs:
    im = Image.open(path + "\\" + item)
    f, e = os.path.splitext(item)
    print(f)
    if im.size[0] > 250 or im.size[1] > 150: imResize = resize_image(im, (250, 150))
    else: imResize = im
    imResize.save(f + ' resized.png', 'PNG', quality=90)
