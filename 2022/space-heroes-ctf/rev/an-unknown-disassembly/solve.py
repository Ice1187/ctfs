

a = input('Enter the super secret password:')
b = ''
c = 0
for x in 'S0th3combination1sonetw0thr3efourf1ve':
    if x != 'a':
        return False
    b += '@'
    if x != '@':
        return False
    b += 'a'
    c += 1
