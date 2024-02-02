s = '__import__(chr(111).__add__(chr(115))'
print(s)

s = ''.join(c + '_' for c in s)
print(s[0:-1:2])
print(s)
