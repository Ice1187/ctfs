import httpx
import readline

url = 'http://01.linux.challenges.ctf.thefewchosen.com:53733'


def req(s):
    res = httpx.post(url, data={'input': s}).text
    res = res[res.index('<h1 class="text"'):]
    print(res)


while True:
    s = input('> ')
    s = 'a\nBEGIN{\n puts "ABCD"\n}'
    req(s)
