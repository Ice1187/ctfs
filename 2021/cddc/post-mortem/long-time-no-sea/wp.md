```
$ mv 0x0702SMIS2.DD 0x0702SMIS2.E01
$ mkdir mnt
$ ewfmount 0x0702SMIS2.E01 mnt
$ mmls mnt/ewf1
$ mkdir /mnt/ewf
$ sudo mount -o -ro,loop,offset=16384 mnt/ewf1 /mnt/ewf
```
reference: https://ubuntuforums.org/showthread.php?t=1576011


Flag(?): {6a1fd570-91dd-413e-993e-4acd5bd4ad64}
