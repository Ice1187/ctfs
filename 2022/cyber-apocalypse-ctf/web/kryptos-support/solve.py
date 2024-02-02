import readline
import requests as rq

url = 'http://188.166.172.138:31979'


def login(user, pswd):
    data = {'username': user, 'password': pswd}
    cookie = {'session': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1vZGVyYXRvciIsInVpZCI6MTAwLCJpYXQiOjE2NTI3MDQ0Mjh9.f8X8HRkk4HXpBg-yVhz0A9gX_G-QUa3JL6QQ5VZLkY0'}
    res = rq.post(f'{url}/api/login', json=data, cookies=cookie)
    print(res.text)
    return res.text


while True:
    try:
        user = input('user> ')  # 'moderator'
        pswd = input('pswd> ')
        login(user, pswd)
    except KeyboardInterrupt:
        break
