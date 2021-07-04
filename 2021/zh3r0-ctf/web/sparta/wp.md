
## .guest.sm\*

There are 4 processes and a user `andrej`, host `DreyAnd` on the machine.

```text
guest_files/.guest.ejs.swm: Vim swap file, version 8.1, pid 3130, user andrej, host DreyAnd, file ~andrej/main/ZH3R0-CTF/sparta/sparta/deployment/views/guest.ejs
guest_files/.guest.ejs.swn: Vim swap file, version 8.1, pid 3019, user andrej, host DreyAnd, file ~andrej/main/ZH3R0-CTF/sparta/sparta/deployment/views/guest.ejs, modified
guest_files/.guest.ejs.swo: Vim swap file, version 8.1, pid 6556, user andrej, host DreyAnd, file ~andrej/main/ZH3R0-CTF/sparta/sparta/deployment/views/guest.ejs
guest_files/.guest.ejs.swp: Vim swap file, version 8.1, pid 7488, user andrej, host DreyAnd, file ~andrej/main/ZH3R0-CTF/sparta/sparta/deployment/views/guest.ejs
```

## TODO
[V] 1. Exploit node-serialize deserialization vuln with `exploit.js` and `solve.py` to gain RCE.
[V] 2. Flag.txt is under / directory.

FLAG: `zh3r0{4ll_y0u_h4d_t0_d0_w4s_m0v3_th3_0bjc3ts_3mper0r}`
