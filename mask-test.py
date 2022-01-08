from PIL import Image, ImageColor

img = Image.open(fp='images/input/tori.jpg', mode='r')

color = input("digite o nome da cor")
color = ImageColor.getrgb(color)
print(color)

color = Image.new('RGB', img.size, color)

#create a mask using RGBA to define an alpha channel to make the overlay transparent
mask = Image.new('RGBA',img.size,(0,0,0,80))

Image.composite(img,color,mask).convert('RGB').show()
