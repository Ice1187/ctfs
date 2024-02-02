from os import popen
from base64 import b64decode, b64encode

cmd = 'date'
print(popen(f'echo -n {cmd} | base64 -d | ./src/webshell').read().strip())
