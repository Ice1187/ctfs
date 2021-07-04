import json

user_db = { 'guest': 'guest', 'admin': 'secret'}

def check(data):
    user = json.loads(data)
    print('json : ', user)
    print('login: ', user_db.get(user['username']) == user['password'])
    print('flag : ', user['showflag'] == True and user['username'] != 'guest')

data = '{"showflag": false, "username": "%s", "password": "%s"}' % (
    'abc", "showflag": true, "abc":"',
    '", "password": null, "abc":"'
)

check(data)

# ref: https://ithelp.ithome.com.tw/articles/10205217
