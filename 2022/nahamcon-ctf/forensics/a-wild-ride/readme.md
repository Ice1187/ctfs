```bash
$ zip2john gpx.zip > gpx.john
$ john --wordlist=/opt/SecLists/Passwords/Leaked-Databases/rockyou.txt ./gpx.john
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
crackme          (gpx.zip)
1g 0:00:00:00 DONE (2022-04-30 15:31) 14.28g/s 14043Kp/s 14043Kc/s 14043KC/s cupucupu..computer?
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
$ unzip gpx.zip
$ unzip -d output gpx.zip
Archive:  gpx.zip
[gpx.zip] ride_1025285.gpx password: crackme
```

Then load the `.gpx` files into [https://gpx.studio](https://gpx.studio) to see the flag.
