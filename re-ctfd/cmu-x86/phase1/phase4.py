def check(n):
    if n < 2:
        return 1
    return check(n-1) + check(n-2)

for i in range(1000):
    if check(i) == 0x37:
        print(i)
        break
