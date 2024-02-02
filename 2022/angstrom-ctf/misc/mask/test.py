import io
import qrcode
import string

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=1, border=0)
while 1:
    inp = bytes.fromhex(input("give input (in hex): "))
    qr.clear()
    qr.add_data(bytes([i for i in inp]))
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    out = [i[:-1] for i in f]
    print(f'out len: {len(out[0])}')
    print('\n'.join(out))
