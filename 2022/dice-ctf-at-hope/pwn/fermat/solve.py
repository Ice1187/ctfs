
for i in range(1, 8):
    print(bin(((2**i)+3)*3).rjust(64, '0'))
print(bin(((2**30)+3)*3).rjust(64, '0'))
print(bin(2147483647).rjust(64, '0'))
