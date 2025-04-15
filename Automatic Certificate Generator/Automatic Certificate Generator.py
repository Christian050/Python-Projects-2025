from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Implementation to genenrate certificate
df = pd.read_csv('list.csv')
font = ImageFont.truetypw('arial.ttf', 60)

for index, j in df.iterrows:
    img = Image.open('Certificate.png')
    draw = ImageDraw.draw(img)
    draw.text(xy=(150, 250))
    text = '{}'.format(j['name'], fill=(0, 0, 0), font=font)
    # Customization
    img.save('pictures/{}.png'.format(j['name']))