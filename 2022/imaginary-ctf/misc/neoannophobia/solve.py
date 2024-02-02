from pwn import *

p = remote('neoannophobia.chal.imaginaryctf.org', 1337)

months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}


def _solve(ans):
    while True:
        p.recvuntil(b'> ')
        date = p.recvuntil(b'\n').strip().split(b' ')
        month = months[date[0].decode()]
        day = int(date[1])
        print(ans.decode(), '--->', month, day)
        if day == 31 or month == 12:
            ans = b'December 31'
            p.sendline(ans)
            return
        elif bool(day == 30) ^ bool(month == 11):
            ans = b'November 30'
            p.sendline(ans)
        elif bool(day == 29) ^ bool(month == 10):
            ans = b'October 29'
            p.sendline(ans)
        elif bool(day == 28) ^ bool(month == 9):
            ans = b'September 28'
            p.sendline(ans)
        elif bool(day == 27) ^ bool(month == 8):
            ans = b'August 27'
            p.sendline(ans)
        elif bool(day == 26) ^ bool(month == 7):
            ans = b'July 26'
            p.sendline(ans)
        elif bool(day == 25) ^ bool(month == 6):
            ans = b'June 25'
            p.sendline(ans)
        elif bool(day == 24) ^ bool(month == 5):
            ans = b'May 24'
            p.sendline(ans)
        elif bool(day == 23) ^ bool(month == 4):
            ans = b'April 23'
            p.sendline(ans)
        elif bool(day == 22) ^ bool(month == 3):
            ans = b'March 22'
            p.sendline(ans)
        elif bool(day == 21) ^ bool(month == 2):
            ans = b'February 21'
            p.sendline(ans)
        elif bool(day == 20) ^ bool(month == 1):
            ans = b'January 20'
            p.sendline(ans)
        else:
            ans = input('> ').strip().encode()
            p.sendline(ans)


def solve(month, day):
    if day < 20:
        ans = b'January 20'
        p.sendline(ans)
    elif day == 20:
        ans = b'February 20'
        p.sendline(ans)
    elif day == 21:
        ans = b'February 21'
        p.sendline(ans)
    elif day == 22:
        ans = b'March 22'
        p.sendline(ans)
    elif day == 23:
        ans = b'April 23'
        p.sendline(ans)
    elif day == 24:
        ans = b'May 24'
        p.sendline(ans)
    elif day == 25:
        ans = b'June 25'
        p.sendline(ans)
    elif day == 26:
        ans = b'July 26'
        p.sendline(ans)
    elif day == 27:
        ans = b'August 27'
        p.sendline(ans)
    elif day == 28:
        ans = b'September 28'
        p.sendline(ans)
    elif day == 29:
        ans = b'October 29'
        p.sendline(ans)
    elif day == 30:
        ans = b'November 30'
        p.sendline(ans)
    elif day == 31:
        ans = b'December 31'
        p.sendline(ans)
        return
    else:
        ans = input('> ').strip().encode()
        p.sendline(ans)
    _solve(ans)


p.recvuntil(b'You may begin')
for r in range(100):
    p.recvuntil(b'----------')
    p.recvuntil(b'----------\n')
    print('Round', r)
    date = p.recvuntil(b'\n').strip().split(b' ')
    month = months[date[0].decode()]
    day = int(date[1])
    print(date)
    solve(month, day)


print(p.recv())
print(p.recv())
