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
from skimage import morphology
from skimage import color


img =io.imread("rena.jpg")
img = color.rgb2gray(img)

eroded_img = morphology.binary_erosion(img)
io.imshow(eroded_img)

dilation_img = morphology.binary_dilation(img)
io.imshow(dilation_img)