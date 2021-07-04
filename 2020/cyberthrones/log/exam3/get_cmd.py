from __future__ import print_function
f = open('./exam3.txt')
data = f.read().split('\n')

count = 0
for l in data:
  count += 1
  lst = l.split(' ')
  c = ''
  for i in range(4, len(lst)):
    c += ' ' + lst[i]
  print(c)
