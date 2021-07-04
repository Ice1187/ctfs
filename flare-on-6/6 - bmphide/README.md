
## 4 - Dnschess
### Description 
> 

### Environment
- [dnSpy](https://github.com/0xd4d/dnSpy)

### Solution

1. `file bmphide.exe` 得知是.NET，所以用打開來看看 `dnSpy`，並往下找到 `ConsoleApp1` -> `ConsoleApp1.exe` -> `BMPHIDE` -> `Program` -> `Main`。
```shell
$ file bmphide.exe
bmphide.exe: PE32 executable (console) Intel 80386 Mono/.Net assembly, for MS Windows
```

2. `bmphide.exe` 是一個指令，第一個參數是讀入bmp的path，第二個參數是讀入data的path，第三個參數是輸出的bmp filename。


### Reference

