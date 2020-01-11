from PIL import ImageFilter
from PIL import Image
import os

img = Image.open("rena.jpg")

blur_rena = img.filter(ImageFilter.GaussianBlur(3))

blur_rena.show()