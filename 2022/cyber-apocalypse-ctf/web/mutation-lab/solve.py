from base64 import b64decode

users = [
    {
        'name': b'AAAAAAAA',
        'session': b'eyJ1c2VybmFtZSI6IkFBQUFBQUFBIn0=',
        'session.sig': b'F2fz7kZhMzGFZIlJ0OlJGnpG4Y4' + b'='
    },
    {
        'name': b'AAAAAAAB',
        'session': b'eyJ1c2VybmFtZSI6IkFBQUFBQUFCIn0=',
        'session.sig': b'y-5m8NuciSWhXsQsMoWYcpkruB0' + b'=',
    },
    {
        'name': b'BBBBBBBB',
        'session': b'eyJ1c2VybmFtZSI6IkJCQkJCQkJCIn0=',
        'session.sig': b'vvolT2USiClwE72L6oM9XboAvhI' + b'='
    }
]

print(users[0]['name'])
print(users[1]['name'])
print(users[0]['session'])
print(users[1]['session'])
print(users[0]['session.sig'])
print(users[1]['session.sig'])
print(b64decode(users[0]['session']))
print(b64decode(users[1]['session']))
print(b64decode(users[0]['session.sig']))
print(len(b64decode(users[0]['session.sig'])))
print(b64decode(users[1]['session.sig']))
