from PIL import Image
img = Image.open("rena.jpg")


import os

print(os.listdir())

#img.show()

crop_rena = img.crop((50,50,500,500))


#crop_rena.show()

img.getpixel((100,100))

gray_rena = img.convert("L")
#gray_rena.show()


rena_200_200 =  img.resize((200,200))

#rena_200_200.show()

rena_90_rotated = img.rotate(90)

#rena_90_rotated.show()


from PIL import ImageEnhance



enhancer = ImageEnhance.Brightness(img)

#enhancer.enhance(2).show()

Contrastenhancer = ImageEnhance.Contrast(img)

#Contrastenhancer.enhance(1.2).show()

#print(img.getpixel((100,100)))

#img.putpixel((100,100),(0,0,0))
#print(img.getpixel((100,100)))


#img.show()