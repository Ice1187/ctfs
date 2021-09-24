# od flag.txt > oddball

with open('oddball', 'r') as f:
    data = f.read()

flag = ''
lines = data.split('\n')
for line in lines:
    words = line.split(' ')[1:]
    for word in words:
        word = hex(int(word, 8))[2:]
        word = ('0' + word)[-4:]
        flag += chr(int(word[2:4], 16))
        flag += chr(int(word[0:2], 16))

print(flag)
