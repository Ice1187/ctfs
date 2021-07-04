f = open('./exam1.txt')
data = f.readlines(220553)

d = {}

for l in data:
  lst = l.split(' ')
  p = lst[3].split(':')[1]
  if p in d:
    d[p] += 1
  else:
    d[p] = 1

print d  
print [ v for v in sorted(d.values())]
  
