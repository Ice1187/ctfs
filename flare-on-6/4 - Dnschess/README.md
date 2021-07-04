
## 4 - Dnschess
### Description 
> Some suspicious network traffic led us to this unauthorized chess program running on an Ubuntu desktop. This appears to be the work of cyberspace computer hackers. You'll need to make the right moves to solve this one. Good luck!

### Environment

- [Ghidra](https://ghidra-sre.org)
- [WireShark](https://www.wireshark.org)
- Scapy
    - `python3 -m pip install scapy`
- Install gtk library
    - `sudo apt install libgtk-3-0`

:::info
#### 將docker的gui導出來mac：
1. mac: 
```shell
brew cask install XQqrtz
brew install socat
open -a XQartz
```
2. docker:
```shell
docker start <docker-name>
docker exec -e DISPLAY=<mac-local-ip>:0 <docker-name> bash 
```

3. mac:
```shell
xhost +<mac-local-ip>
```

4. docker:
```shell
/path/to/the/<gui-program>
```
- Ref
    - [Running GUI’s with Docker on Mac OS X](https://cntnr.io/running-guis-with-docker-on-mac-os-x-a14df6a76efc)
    - [Running Chromium inside Docker - Gtk: cannot open display: :0
](https://stackoverflow.com/questions/28392949/running-chromium-inside-docker-gtk-cannot-open-display-0/28395350#28395350)

:::

### Solution

1. `ChessUI`跑起來，一玩就 resigned。再看看`capture.pcap`，DNS封包裡帶有一些下西洋棋的指令

![](https://i.imgur.com/AhUqCoL.png)

2. 逆一下`ChessAI.so`，發現`getNextMove`對一串字串作xor，然後接到`@flare-on.com`字串前面。所以這裡就是flag了
 
![](https://i.imgur.com/arNa5yx.png)

![](https://i.imgur.com/cJnmGY0.png)

3. `phVar2`是 hostent 結構儲存 host info；`pcVar1`是 4bytes表示 ip；`param1` 是flag 字串的 index。所以通過 if 的條件：
    - hostent sucess
    - ip[0] == 127 
    - ip[3] & 1 == 0
    - ip[2]的low 4 bits == 設定的idx

![](https://i.imgur.com/ouT5krY.png)


4. 寫 script 從封包裡把ip拉出來，然後 xor 回去，GET FLAG。
```python3
from scapy.all import *

p = rdpcap('./capture.pcap')
ip = []
for i in range(0, len(p), 2):
    ip.append(list(map(int, p[i+1][DNSRR].rdata.split('.'))))

ip2 = []
for i in ip:
    if (i[3] & 0x1) == 0:
       ip2.append(i)

ip2 = sorted(ip2, key=lambda x: (x[2] & 0xf))

flag = ''
data = '795ab8bcecd3dfdd99a5b6ac1536858d090877524d71547da7a70816fdd7'
for i in range(0, len(ip2)):
    idx = i*2*2
    flag += chr(ip2[i][1] ^ int(data[idx:idx+2], 16))
    idx = (i*2+1)*2
    flag += chr(ip2[i][1] ^ int(data[idx:idx+2], 16))

flag += '@flare-on.com'
print(flag)
```

FLAG: `LooksLikeYouLockedUpTheLookupZ@flare-on.com`


### Reference
- [Running GUI’s with Docker on Mac OS X](https://cntnr.io/running-guis-with-docker-on-mac-os-x-a14df6a76efc)
- [Running Chromium inside Docker - Gtk: cannot open display: :0
](https://stackoverflow.com/questions/28392949/running-chromium-inside-docker-gtk-cannot-open-display-0/28395350#28395350)
- [GTK+ 3 Reference Manual](https://developer.gnome.org/gtk3/stable/)
- [Reading PCAP file with scapy](https://stackoverflow.com/questions/42963343/reading-pcap-file-with-scapy)

