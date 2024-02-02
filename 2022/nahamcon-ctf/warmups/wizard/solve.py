from base64 import b64decode


def stage1(bin_str):
    n = int(bin_str, 2)
    ans = n.to_bytes(64, 'big').strip()
    print(ans.decode())


def stage2(hex_str):
    n = int(hex_str, 16)
    ans = n.to_bytes(64, 'big').strip()
    print(ans.decode())


def stage3(oct_str):
    n = int(oct_str, 8)
    ans = n.to_bytes(64, 'big').strip()
    print(ans.decode())


def stage4(int_str):
    n = int(int_str, 10)
    ans = n.to_bytes(64, 'big').strip()
    print(ans.decode())


def stage5(b64_str):
    ans = b64decode(b64_str)
    print(ans.decode())


def stage6(big_str):
    n = int(big_str, 16)
    ans = n.to_bytes(64, 'little').strip()
    print(ans.decode())


stage1('010110100110010101110010011011110111001100100000001001100010000001001111011011100110010101110011')
stage2('4f6820776f77777721204261736520313020697320636f6f6c20616e6420616c6c2062757420486578787878')
stage3('535451006154133420162312701623127154533472040334725553046256234620151334201413347444030460563312201673122016730267164')
stage4('8889185069805239596091046045687553579520816794635237831028832039457')
stage5('QmFzZXMgb24gYmFzZXMgb24gYmFzZXMgb24gYmFzZXMgOik=')
stage6('293a2065636e657265666669642065687420776f6e6b206f7420646f6f672073277449')
