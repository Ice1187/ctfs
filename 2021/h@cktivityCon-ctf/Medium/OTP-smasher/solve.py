# source .pyenv/bin/activate; python3.6 solve.py
from PIL import Image
import requests
import pytesseract

url = 'http://challenge.ctf.games:30212' + '/static/otp.png'

img = Image.open(requests.get(url, stream=True).raw)
text = pytesseract.image_to_string(img, lang='eng')
print(text)
