f = open('./exam2.txt')
data = f.read().split('\n')

d = {}

count = 0
for l in data:
  count += 1
  lst = l.split(' ')
  if(count != len(data)):
    p = lst[1].split(':')[0]
  if p in d:
    d[p] += 1
  else:
    d[p] = 1

print len(data)
print d
print [ v for v in sorted(d.values())]
