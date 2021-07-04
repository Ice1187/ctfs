from __future__ import print_function
f = open('./exam3.txt')
data = f.read().split('\n')

count = 0
for l in data:
  count += 1
  lst = l.split(' ')
#  print('len: '+str(len(lst)), lst)
  if len(lst) <= 8:
    continue
  if lst[8].startswith('command'):
    c = ''
    for i in range(8, len(lst)):
      c += ' ' + lst[i]
    print(c)
