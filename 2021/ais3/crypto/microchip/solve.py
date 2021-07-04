enc_flag = "=Js&;*A`odZHi'>D=Js&#i-DYf>Uy'yuyfyu<)Gu"

l = ['', '', '', '']
for i in range(0, len(enc_flag), 4):
    for j in range(4):
        l[3-j] += enc_flag[i+j]

def decode(l, head):
    for key in range(96):
        s = ''
        for i in l:
            num = ord(i) - 32
            num = (num + key) % 96
            num = num + 32
            s += chr(num)
        
        if s[0] == head:
            print(s)
            return s

ll = [
    decode(l[0], 'A'),
    decode(l[1], 'I'),
    decode(l[2], 'S'),
    decode(l[3], '3')
]

flag = ''
for i in range(len(ll[0])):
    for j in range(4):
        flag += ll[j][i]

print(flag)

