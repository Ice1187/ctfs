with open('./output', 'r') as f:
    data = f.read()

flag = ''
for s in data.strip().split('\n'):
    if len(s) == 1:
        flag += (s)

print(flag)
