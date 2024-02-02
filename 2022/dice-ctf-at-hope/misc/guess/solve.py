from PIL import (Image, ImageDraw)

IMAGE_PATH = './output.png'

with Image.open(IMAGE_PATH) as image:
  width, height = image.size
  mode = image.mode
  data = list(image.getdata())

flag_data = []
for pixel in data:
  a = pixel[0] & 1
  b = pixel[1] & 1
  c = (pixel[2] & 1) ^ a ^ b
  flag_data.append((a*200, b*200, c*200, pixel[3]))

flag_image = Image.new(mode, (width, height))
flag_image.putdata(flag_data)
flag_image.save('flag.png')




