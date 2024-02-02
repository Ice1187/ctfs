from PIL import Image

img = Image.open('./modifiedflag.png')

pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b, a = pixels[i, j]
        pixels[i, j] = (r, g+68, b+129, 255)

img.save('solve.png')
