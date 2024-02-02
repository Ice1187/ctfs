import readline

workable = "ababc');--;)'cbaba"


def rev(cmd):
    rev_cmd = cmd
    rev_cmd = rev_cmd + rev_cmd[::-1]
    print(rev_cmd)
    return rev_cmd


while True:
    #cmd = input('> ')
    cmd = "' || (SELECT flag FROM flags));-- -"
    rev(cmd)
    break
