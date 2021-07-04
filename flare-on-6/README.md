Flare-On 6 writeup
===

[TOC]

---

## 0 - Writeup Links
- [Offcial Writeup](https://www.fireeye.com/blog/threat-research/2019/09/2019-flare-on-challenge-solutions.html)
- [Hackmd version](https://hackmd.io/@Ice1187/flare-on-6-writeup)

---

## 1 - Memecat Battlestation

- password for 7z: `flare`

雖然沒有寫過 .NET, C# 的東西，但第一關矇矇混混地看一看，還是解出來了 XD

### Description
> Welcome to the Sixth Flare-On Challenge! 
> 
> This is a simple game. Reverse engineer it to figure out what "weapon codes" you need to enter to defeat each of the two enemies and the victory screen will reveal the flag. Enter the flag here on this site to score and move on to the next level.
> 
> * This challenge is written in .NET. If you don't already have a favorite .NET reverse engineering tool I recommend dnSpy
> 
> ** If you already solved the full version of this game at our booth at BlackHat  or the subsequent release on twitter, congratulations, enter the flag from the victory screen now to bypass this level.
> 

### Environment

如題所述，安裝 [dnSpy](https://github.com/0xd4d/dnSpy) 就可以解了

### Solution

將 .exe 丟進 dnSpy，根據直覺依序點入`MemeCatbattlestation (1.0.0.0) -> MemeCatbattlestation.exe -> MemeCatbattlestation`，看到`Stage1Form`和`Stage2Form`應該就是題目裡的兩個關卡。

#### Stage 1

1. 點入`Stage1Form`，因為要找 "weapon code to defeat enemies"，直覺點開`FireButton_Click`

```csharp=
private void FireButton_Click(object sender, EventArgs e)
{
    if (this.codeTextBox.Text == "RAINBOW")
    {
        this.fireButton.Visible = false;
```
2. 第一個 weapon code 就是 "RAINBOW"

#### Stage 2

1. 點開`Stage2Form`，一樣先看`FirrButton_Click`

```csharp=
private void FireButton_Click(object sender, EventArgs e)
{
    if (this.isValidWeaponCode(this.codeTextBox.Text))
    {
        this.fireButton.Visible = false;
```

2. 再點入`isValidWeaponCode()`

```csharp=
private bool isValidWeaponCode(string s)
    {
    	char[] array = s.ToCharArray();
    	int length = s.Length;
    	for (int i = 0; i < length; i++)
    	{
            char[] array2 = array;
            int num = i;
            array2[num] ^= 'A';
    	}
    	return array.SequenceEqual(new char[]
    	{
            '\u0003',
            ' ',
            '&',
            '$',
            '-',
            '\u001e',
            '\u0002',
            ' ',
            '/',
            '/',
            '.',
            '/'
        });
    }
```

3. 根據程式碼，`weapon code == ("AAAAAAAAAAAA" ^ 0x032026242d1e02202f2f2e2f )`，即 "Bagel_Cannon"
4. 輸入完weapon code，勝利畫面即有flag

FLAG: `Kitteh_save_galixy@flare-on.com`

---

## 2 - Overlong

- password for 7z: `flare`

### Description

> The secret of this next challenge is cleverly hidden. However, with the right approach, finding the solution will not take an <b>overlong</b> amount of time.

### Environment


### Solution




### Unintended Solution
- r2打開來看，直接噴出flag

![](https://i.imgur.com/YknCnQe.jpg)

FLAG: `I_a_M_t_h_e_e_n_C_o_D_i_n_g@flare_on.com`

---

## 3 - Flarebear

- password for 7z: `flare`

### Description 
> We at Flare have created our own Tamagotchi pet, the flarebear. He is very fussy. Keep him alive and happy and he will give you the flag.

### Environment 

#### Decompiler
- [jadx](https://github.com/skylot/jadx)

#### Emulator
- [Android Studio](https://developer.android.com/studio)
- 從`AVD Manager` 一個 device（我用 Google Pixel 3a），然後把模擬器跑起來
- 把`flarebear.apk`直接拖進模擬器，會自動安裝
 

### Solution

1. 用`jadx-gui`打開`flarebear.apk`。
2. 一般來說，App 會從`MainActivity`開始執行，裡面就是一些首頁的基本功能。
3. 下一個看`FlareBearActivity`，內容大概是玩遊戲時的各種功能。其中看到`danceWithFlag()`，往前追到`setMood()`，發現要符合`isHappy()`和`isEcstatic()`。

![](https://i.imgur.com/QOaMHRR.png)

4. `isHappy()`必須滿足`getStat()`；`isEcstatic()`必須滿足`getState()`組成的條件。
![](https://i.imgur.com/Vm7sDH3.png)

#### `isHappy()`
- 根據上圖的code，在`activity`這個 string 裡，(f的數量/p的數量) 必須介於2.0~2.5。
    - 參考 [使用SharedPreference儲存資料](https://ithelp.ithome.com.tw/articles/10188441)

- `jadx`搜尋"activity"，找到`saveActivity()`會呼叫`setState()`，用不斷append的方式來修改`activity`的值。
![](https://i.imgur.com/HTqERGR.png)
- 發現`feed()`、`play()`、`clean()`分別會呼叫`saveActivity()`來寫"f"、"p"、"c"。
![](https://i.imgur.com/tFaQezo.png)
- 所以`isHappy()`的條件：「(餵食次數/玩的次數) 要介於2.0~2.5之間」

#### `isEcstatic()`
- `changeMass()`、`changeHappy()`、`changeClean()`負責修改`mass`、`happy`、`clean`的值
- `feed()`、`play()`、`clean()`對`mass`、`happy`、`clean`有不同權重的影響
    - feed: mass(10), happy(2), clean(-1)
    - play: mass(-2), happy(4), clean(-1)
    - clean: mass(0), happy(-1), clean(6)
![](https://i.imgur.com/MJfWLYe.png)
![](https://i.imgur.com/d9Lc1Ow.png)
- `isEcstatic()`的條件：「mass == 72 && happy == 30 && clean == 0」

5. 令feed為x，play為y，clean為z，解聯立方程式，得解為「x=8，y=4，z=2」。先按x跟y，再按z，以符合`isHappy()`的條件
![](https://i.imgur.com/cs0wIsI.png)
6. 按順序輸入即得Flag

FLAG: `th4t_was_be4rly_a_chall3nge@flare-on.com`

### Reference
- [Android Applications Reversing 101](https://www.evilsocket.net/2017/04/27/Android-Applications-Reversing-101/)
- [ApkTool项目解析resources.arsc详解](https://juejin.im/post/5ae8b2b26fb9a07abf724ebf)
    - 追apktool的src code，解釋resources.arsc的檔案結構，及apktool怎麼解析resources.arsc
- [checkExpressionValueIsNotNull()](https://github.com/JetBrains/kotlin/blob/master/libraries/stdlib/jvm/runtime/kotlin/jvm/internal/Intrinsics.java)
    - Source Code，那時候不知道這 function 在幹嘛
    - 看懂 String expression 那邊的錯誤資訊，在理解code上有不小幫助 XD
- [使用SharedPreference儲存資料](https://ithelp.ithome.com.tw/articles/10188441)
    - 研究一下 getDefaultSharedPreferences() 怎麼存/讀資料
- [Android Developer Guide](https://developer.android.com/guide)


> ### Extra Learning
> #### Apktool
> ##### Install
> - 沒有java，先裝java (jre: java runtime environment)
> ```shell
> sudo apt update
> sudo apt install default-jre
> ```
> - 裝 [apktool](https://ibotpeaches.github.io/Apktool/)。
> ##### Usage
> - `apktool d Flarebear.apk`
>     - apktool automatically decompiles > `AndroidManifest.xml`, `resources.arsc`, and converts `classes.dex` to an intermediary language called SMALI, an ASM-like language used to represent the Dalvik VM opcodes as a human readable language.
    - `smali/` = `unzip file.apk` + `jadx classes.dex`

---

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

---

## 5 - demo

- password for 7z: `flare`

[murmur]

### Description
> 

### Environment



### Solution


---

## 6 - bmphide

- password for 7z: `flare`

[murmur]

### Description
> Tyler Dean hiked up Mt. Elbert (Colorado's tallest mountain) at 2am to capture this picture at the perfect time. Never skip leg day. We found this picture and executable on a thumb drive he left at the trail head. Can he be trusted?

### Environment

### Solution


1. `stegsolve` 先把 `image.png` 開起來看，好像有藏東西。但 `binwalk` 和 `dd` 試了一下，看不出什麼。 

![](https://i.imgur.com/Q4f42AE.jpg)

2. 把 `bmphide.exe` 丟進 `ghidra`。裡面連結到 `MSCOREE.DLL` (Microsoft .NET Runtime Execution Engine)，所以應該是個 .NET 檔。



--- 

