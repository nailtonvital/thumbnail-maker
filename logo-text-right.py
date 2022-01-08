from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters
import textwrap

img = Image.open(fp='images/input/tori.jpg', mode='r')

font = ImageFont.truetype(font='../assets/fonts/Impact.ttf', size=200)

draw = ImageDraw.Draw(im=img)

# Define our text / / 40 characters limit
text = """Lorem ipsum dolor sit amet orci aliquam."""

# Calculate the average length of a single character of our font.
# Note: this takes into account the specific font and font size.
avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)

# Translate this average length into a character count
max_char_count = int(img.size[0] * .618 / avg_char_width)

# Create a wrapped text object using scaled character count
text = textwrap.fill(text=text, width=max_char_count)
# Add text to the image
draw.text(xy=(img.size[0]/1.5, img.size[1] / 2), text=text, font=font, anchor='mm')
# view the result
logo = Image.open('images/input/logo/country/french.png')
logo = logo.resize((550, 550))
img.paste(logo, (170, 270), logo)

img.show()
