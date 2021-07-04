s = 'AlS3{BasE64_i5+b0rNIng~\Qwo/-xH8WzCj7vFD2eyVktqOL1GhKYufmZdJpX9}'
enc_c = '423560343444373134655114504577415715745143147321'
enc_r = '000101000101000000000000001100000011010101010000'
enc_f = 'BgiJ6\\w1Aj\\1guikl7xiXKIhXKil6fo65Kn87B-8warzK==='

flag = 'AIS3{base1024_15_c0l0RFuL_GAM3_CL3Ar_thIS_IS_y0Ur_FlaG!}'

def getStr(s):
    ret = ''
    for c in s:
        b = bin(ord(c))[2:].rjust(8, '0')
        ret += b
    l = (len(ret) % 10) / 2 - 1
    if l != -1:
        ret += '0'*(10 - (len(ret) % 10))
    # print(ret)
    return ret

def getNum(input_):
    bs = getStr(input_)
    # print(len(bs), bs)
    l = [bs[x:x+10] for x in range(0, len(bs), 10)]
    # print(l)
    l = [int(x, 2) for x in l]
    # print(l)
    c = ''
    r = ''
    f = ''
    for num in l:
        c += str((num >> 0x6) & 0x7)
        r += str(num >> 9)
        f += s[num & 0x3f]

    # print(flag)
    return (c, r, f)

offset = 1
l = len(flag)
bb = 0
for i in range(32, 127):
    for j in range(32, 127):
        f = flag + chr(i) + chr(j) 
        c, r, ff = getNum(f)
        print(f[-5:], c, r, ff)
        print(' '*len(f[-5:]), enc_c[:len(c)], enc_r[:len(r)], enc_f[:len(ff)])
        '''
            if (l+1)%4 == 0:
                # print(c[:-1], r[:-1], ff[:-1])
                # print(enc_c[:l-offset], enc_r[:l-offset], enc_f[:l-offset])
                # print(c[:-1] == enc_c[:l-offset], r[:-1] == enc_r[:l-offset], ff[:-1] == enc_f[:l-offset])
                if c[:-1] == enc_c[:l-offset] and r[:-1] == enc_r[:l-offset] and ff[:-1] == enc_f[:l-offset]:
                    print('[+]: ' + chr(i), ff[:])
                    flag += chr(i)
                    bb = 1
                    offset += 1
                    break
            else:
                # print(len(c[:-1]))
                # print(len(enc_c[:l-offset]))
                if c[:] == enc_c[:l-offset] and r[:] == enc_r[:l-offset] and ff[:-1-offset] == enc_f[:l-1]:
                    print('[+]: ' + chr(i), ff[:])
                    flag += chr(i)
                    bb = 1
                    break
                '''
        '''
        if bb == 1:
            break
        '''

        '''
            if (l+1)%4 == 0:
                if c[:-1] == enc_c[:l] and r[:-1] == enc_r[:l] and ff[:-1] == enc_f[:l]:
                    print('[+]: ' + chr(i), ff[:])
                    flag += chr(i)
                    bb = 1
                    break
            if (l+1)%4 == 1:
                if c[:] == enc_c[:l+1] and r[:] == enc_r[:l+1] and ff[:-1] == enc_f[:l]:
                    print(chr(i), ff[:])
                    flag += chr(i)
                    bb = 1
                    break
            if (l+1)%4 == 2:
                if c[:] == enc_c[:l+1] and r[:] == enc_r[:l+1] and ff[:-1] == enc_f[:l]:
                    print(chr(i), ff[:])
                    flag += chr(i)
                    bb = 1
                    break
            if (l+1)%4 == 2:
                if c[:] == enc_c[:l] and r[:] == enc_r[:l] and ff[:-1] == enc_f[:l-1]:
                    print('[+]: ' + chr(i), ff[:])
                    flag += chr(i)
                    bb = 1
                    break
            if (l+1)%4 == 3:
                if c[:] == enc_c[:l+1] and r[:] == enc_r[:l+1] and ff[:-1] == enc_f[:l]:
                    print('[+]: ' + chr(i), ff[:])
                    flag += chr(i)
                    bb = 1
                    break
            else:
                if c[:-1] == enc_c[:l+1] and r[:-1] == enc_r[:l+1] and ff[:-1] == enc_f[:l+1]:
                    print(chr(i), ff[:-1])
                    flag += chr(i)
                    bb = 1
                    break
        '''
