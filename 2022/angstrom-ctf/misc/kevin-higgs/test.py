#!/usr/local/bin/python3

import pickle
import io
import sys

module = type(__builtins__)
empty = module("empty")
empty.empty = empty
sys.modules["empty"] = empty


class SafeUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        print(f'[*] module: {module}')
        print(f'[*] name: {name}')
        return super().find_class(module, name)


lepickle = bytes.fromhex(input("Enter hex-encoded pickle: "))
if len(lepickle) > 400:
    print("your pickle is too large for my taste >:(")
else:
    tmp = SafeUnpickler(io.BytesIO(lepickle))
    print('here')
    tmp.load()
