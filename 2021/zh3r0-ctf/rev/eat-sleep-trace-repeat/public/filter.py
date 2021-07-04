with open('./out_3.txt', 'rb') as f:
    data = f.read()

data = data.split(b'\n')

s = ''
for i in data:
    try:
        c = i.decode('ascii')
        if c.isprintable():
            s += c
    except:
        continue
print(''.join(sorted(s)))
