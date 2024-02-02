from base64 import b64decode


def decrypt(data, key):
    '''
    function encr {
        param(
            [Byte[]]$data,
            [Byte[]]$key
          )

        [Byte[]]$buffer = New-Object Byte[] $data.Length
        $data.CopyTo($buffer, 0)

        [Byte[]]$s = New-Object Byte[] 256;
        [Byte[]]$k = New-Object Byte[] 256;

        for ($i = 0; $i -lt 256; $i++)
        {
            $s[$i] = [Byte]$i;
            $k[$i] = $key[$i % $key.Length];
        }

        $j = 0;
        for ($i = 0; $i -lt 256; $i++)
        {
            $j = ($j + $s[$i] + $k[$i]) % 256;
            $temp = $s[$i];
            $s[$i] = $s[$j];
            $s[$j] = $temp;
        }

        $i = $j = 0;
        for ($x = 0; $x -lt $buffer.Length; $x++)
        {
            $i = ($i + 1) % 256;
            $j = ($j + $s[$i]) % 256;
            $temp = $s[$i];
            $s[$i] = $s[$j];
            $s[$j] = $temp;
            [int]$t = ($s[$i] + $s[$j]) % 256;
            $buffer[$x] = $buffer[$x] -bxor $s[$t];
        }

        return $buffer
    }
    '''
    buf = bytearray(data)
    s = [None for _ in range(256)]
    k = [None for _ in range(256)]

    for i in range(0, 256):
        s[i] = i
        k[i] = key[i % len(key)]

    j = 0
    for i in range(0, 256):
        j = (j + s[i] + k[i]) % 256
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp

    i = 0
    j = 0
    for x in range(len(buf)):
        i + (i+1) % 256
        j = (j+s[i]) % 256
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        t = (s[i] + s[j]) % 256
        buf[x] = buf[x] ^ s[t]

    return buf


for encoding in ['ascii', 'utf_7', 'utf_8', 'utf_8_sig', 'utf_16_le', 'utf_16_be', 'utf_16', 'utf_32', 'utf_32_le', 'utf_32_be', 'cp_1252']:
    try:
        key = list('Q0mmpr4B5rvZi3pS'.encode(encoding))
        enc = 0xF844A6035CF27CC4C90DFEAF579398BE6F7D5ED10270BD12A661DAD04191347559B82ED546015B07317000D8909939A4DA7953AED8B83C0FEE4EB6E120372F536BC5DC39CC19F66A5F3B2E36C9B810FE7CC4D9CE342E8E00138A4F7F5CDD9EED9E09299DD7C6933CF4734E12A906FD9CE1CA57D445DB9CABF850529F5845083F34BA1C08114AA67EB979D36DC3EFA0F62086B947F672BD8F966305A98EF93AA39076C3726B0EDEBFA10811A15F1CF1BEFC78AFC5E08AD8CACDB323F44B4DD814EB4E244A153AF8FAA1121A5CCFD0FEAC8DD96A9B31CCF6C3E3E03C1E93626DF5B3E0B141467116CC08F92147F7A0BE0D95B0172A7F34922D6C236BC7DE54D8ACBFA70D184AB553E67C743BE696A0AC80C16E2B354C2AE7918EE08A0A3887875C83E44ACA7393F1C579EE41BCB7D336CAF8695266839907F47775F89C1F170562A6B0A01C0F3BC4CB
        data = enc.to_bytes(0x1000, 'big').strip(b'\x00')
        res = decrypt(data, key)
        print(res)
        print('==============', res.decode(encoding))
    except:
        pass
