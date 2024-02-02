import requests as rq

url = 'https://crumbs.web.actf.co'

data = ''
for i in range(1002):
    data = rq.get(f'{url}/{data}').text
    print(i, data)
    data = data[data.find('Go to ')+len('Go to '):]
