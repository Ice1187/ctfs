from pprint import pp


def count(text, alphabet):
    print('---- Count ----')
    d = {}
    for c in alphabet:
        d[c] = text.count(c)
    d = {k: v for k, v in sorted(
        d.items(), key=lambda item: item[1], reverse=True)}
    pp(d)
    print('')


with open('./output.txt', 'r') as f:
    ct = f.read()

alphabet = set(ct) - {'\n'}
mapping = {
    'h': 'h',
    'w': 'o',
    'f': 'p',
    'y': 'e',
    'A': '{',
    'v': 'm',
    'p': 'o',
    'u': '}',
    'g': ' ',
    'a': 'B',
    'k': 't',
    '"': 'a',
    'n': 'E',
    '_': 's',
    'q': 'i',
    'S': 'n',
    'i': 'l',
    'c': 'f',
    't': 'y',
    'l': 'u',
    'j': 'b',
    'T': '_',
    'd': 'd',
    'o': 'A',
    'V': 'v',
    ',': 'x',
    's': 'c',
    '.': 'r',
    '}': 'm',
    'O': 'V',
    'M': 'g',
    'B': '.',
    'r': ',',
    ' ': 'w',
    'I': 'j',
    'x': 'I',
    'e': 'q',
    'b': '"',
    'E': 'k',
    'm': 'S',
    '{': 'T',
}
assert any([values for key, values in mapping.items()
           if len(values) > 1]) == False

count(ct, alphabet)
print([c for c in alphabet if c not in mapping.values()])

pt = ''
for c in ct:
    if c in mapping.keys():
        pt += f'\033[33m{mapping[c]}\033[0m'
    else:
        pt += c

print(pt)
