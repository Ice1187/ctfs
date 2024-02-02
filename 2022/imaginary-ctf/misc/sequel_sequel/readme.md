Use ssh local port forwarding to access `127.0.0.1:3306` on the server, then query the `ictf` table to get the flag.

```
$ sudo ssh -L 3306:127.0.0.1:3306 -p 42022 -N ethan@chal.imaginaryctf.org
$ mysql -u ethan -p -h 127.0.0.1 ictf
mysql> select * from ictf;
+----------------------------------------------+
| flag                                         |
+----------------------------------------------+
| ictf{ssH_p0rt_f0rw4rding_1s_uSeful_0eb24f93} |
+----------------------------------------------+
```
