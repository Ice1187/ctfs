#!/usr/bin/env python3

while True:
    a = input(">>> ")
    print(n in "()abcdefghijklmnopqrstuvwxyz" for n in a)
    assert all(n in "()abcdefghijklmnopqrstuvwxyz" for n in a)
    exec(a)
