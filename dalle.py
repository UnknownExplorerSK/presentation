import os
import openai
import requests
from PIL import Image
import shutil
import urllib
import time
import collections 
import collections.abc
from pptx import Presentation
from pptx.util import Inches

var = input("Please enter your api key: ")
openai.api_key = var
openai.Model.list()
#print(openai.api_key)

response = openai.Image.create(
  prompt="a cute wild animal playing the trumpet",
  n=1,
  size="256x256"
)
image_url = response['data'][0]['url']
print(image_url)

time.sleep(1)

# openai.Image.create(
#     prompt="a cute wild animal playingt the trumpet",
#     n=1,
#     size="512x512"
# )

response = requests.get(image_url)
if response.status_code:
    fp = open('dall_e_generated_image.png', 'wb')
    fp.write(response.content)
    fp.close()

# time.sleep(1)

# image = Image.open('dall_e_generated_image.png')
# new_image = image.resize((400,200))
# new_image.save('dalle_new_image.png')

# img1 = 'dalle_new_image.png'