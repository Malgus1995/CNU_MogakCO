from PIL import ImageFilter
from PIL import Image
import os

img = Image.open("ari.jpg")

from PIL import ImageFilter
from PIL import Image
import os

rena = Image.open("rena.jpg")

#ari_rena = img.filter(ImageFilter.GaussianBlur(3))


blur_ari = img.filter(ImageFilter.MedianFilter(7))

blur_rena = rena.filter(ImageFilter.MedianFilter(7))


from skimage import io
from skimage.morphology import disk
from skimage import color
from skimage import filters

img =io.imread("rena.jpg")
img = color.rgb2gray(img)

out = filters.median(img,disk(7))

io.imshow(out)
io.show()