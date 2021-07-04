## 1.
```
$ ./gdc_exec sh
$ cat flag
```

## 2.

## 3.
1. Do some fuzzing
```
input> "

Exception:
EOF while scanning triple-quoted string literal (<string>, line 1)
input> """"""

Program output:
```
2. So we are in a situation like: `f"""Program output: {input}"""`

