from skimage import io, color
img = io.imread("rena.jpg")
#io.imshow(img)
#io.imsave("duple_rena.jpg",img)

rena_hsv = color.rgb2hsv(img)
#io.imshow(rena_hsv)

import numpy as np

from skimage import io,draw

npimg =np.zeros((100,100),dtype=np.uint8)

x,y = draw.circle(50,50,10)

#npimg[x,y]=1

#io.imshow(img)

epx,epy = draw.ellipse(50,50,10,20)

npimg[epx,epy] =1

#io.imshow(npimg)

polyimg = np.zeros((100,100),dtype=np.uint8)

r =np.array([10,25,80,50])
c =np.array([10,60,40,10])

x,y = draw.polygon(r,c)

polyimg[x,y] = 1
io.imshow(polyimg)



