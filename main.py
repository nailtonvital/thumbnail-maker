from PIL import Image, ImageDraw, ImageFont, ImageColor
from string import ascii_letters
import textwrap
import requests
import os

# IMAGE AREA
print("choose the background image.".upper())

keyword = str(input("Type a keyword of image:"))

if " " in keyword:
    keyword = keyword.replace(' ', '-')

url = f"https://source.unsplash.com/1980x1080/?{keyword}"

img = Image.open(requests.get(url, stream=True).raw)

# Mask Area
print("Do you want a mask? (y/n)")
confirm = None
while confirm is None:
    choice = str(input(">"))
    if choice == "y" or choice == "n":
        confirm = True
    else:
        pass

if choice == "y":
    color = input("Type the color name:\n>")
    color = ImageColor.getrgb(color)
    print(color)

    color = Image.new('RGB', img.size, color)

    #create a mask using RGBA to define an alpha channel to make the overlay transparent
    mask = Image.new('RGBA',img.size,(0,0,0,200))

    mask = Image.composite(img,color,mask).convert('RGB')
    img.paste(mask)
# LOGO
print("Do you want a logo? (y/n)")
confirm = None
while confirm is None:
    choice = str(input(">"))
    if choice == "y" or choice == "n":
        confirm = True
    else:
        pass

if choice == "y":
    dataFiles = os.listdir('images/input/logo')

    print("Choose:")
    for data in dataFiles:
        print(data)

    confirm = None
    while confirm is None:
        try:
            logos = input(">")
            logoFiles = os.listdir(f'images/input/logo/{logos}')
            if logoFiles:
                confirm = True
        except:
            print("Not found")

    for logo in logoFiles:
        print(logo)

    confirm = None
    while confirm is None:
        try:
            logo = input(">")
            logoFile = Image.open(f'images/input/logo/{logos}/{logo}')
            if logoFile:
                confirm = True
        except:
            print("Not found")

    logo = logoFile.resize((550, 550))
    img.paste(logo, (170, 270), logo)

    # TEXT AREA
    txt = str(input("Type the text for the thumbnail:"))

    limit = 40
    while len(txt)>limit:
        txt = str(input(f"The text cant have more than {limit} characters:"))

    font = ImageFont.truetype(font='fonts/Impact.ttf', size=200)

    draw = ImageDraw.Draw(im=img)

    # Define our text / / 40 characters limit
    text = txt

    # Calculate the average length of a single character of our font.
    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)

    # Translate this average length into a character count
    max_char_count = int(img.size[0] * .618 / avg_char_width)

    # Create a wrapped text object using scaled character count
    text = textwrap.fill(text=text, width=max_char_count)
    # Add text to the image
    draw.text(xy=(img.size[0]/1.5, img.size[1] / 2), text=text, font=font, anchor='mm')

    img.save(f"images/results/{keyword}-logo.jpg")
else:
    # TEXT AREA
    txt = str(input("Type the text for the thumbnail:"))

    limit = 92
    while len(txt)>limit:
        txt = str(input(f"The text cant have more than {limit} characters:"))

    font = ImageFont.truetype(font='fonts/Impact.ttf', size=150)

    draw = ImageDraw.Draw(im=img)

    text = txt

    # Calculate the average length of a single character of our font.
    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)

    # Translate this average length into a character count
    max_char_count = int(img.size[0] * .9 / avg_char_width)

    # Create a wrapped text object using scaled character count
    text = textwrap.fill(text=text, width=max_char_count)

    # Add text to the image
    draw.text(xy=(img.size[0]/2, img.size[1] / 2), text=text, font=font, align='center', anchor='mm')
    img.save(f"images/results/{keyword}.jpg")


