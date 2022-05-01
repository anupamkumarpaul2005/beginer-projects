import requests
import io
from PIL import Image, ImageFont, ImageDraw
import textwrap
import numpy as np
import imageio
import discord

while True:
    response = requests.get("https://programming-quotes-api.herokuapp.com/quotes/random")
    quote = response.json()["en"]
    if len(quote)<150:
        break
author = response.json()["author"]
text = quote+"\n-"+author
text = textwrap.fill(text=text, width=40)
image = requests.get("https://picsum.photos/500")
font = ImageFont.truetype(font='/resources/Astral Sisters.ttf', size=38)
img = io.BytesIO(image.content)
f = imageio.imread(img, as_gray=True)
img2 = Image.open(img)
img_edit = ImageDraw.Draw(img2)
if np.mean(img2) > 127:
    img_edit.text((20,150), text, font=font, fill=(0,0,0), align="center")
else:
    img_edit.text((20, 150), text, font=font, fill=(255,255,255), align="center")
# img2.show()

client = discord.Client(activity=discord.Game(name='my game'))
user = client.get_user(740833653831106661)
user.send()