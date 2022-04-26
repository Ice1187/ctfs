## level 1
### stage 1
#print(getattr(getattr('Hello, ', '__add__')(input()), '__add__')('!'))
### stage 2
#list(map(print, (map(getattr('Hello, {}!', 'format') ,getattr(getattr(getattr(open(0), 'read')(), 'strip')(), 'split')('\n')))))

'''
n = lambda n: int(getattr((getattr(0.4472135954999579, '__mul__')(pow(1.618033988749895, n))), '__add__')(0.5))
fib = [0, 1]
for i in range(2, 71):
  cal = n(i)
  fib.append(fib[i-2]+fib[i-1])
  if cal != fib[i]:
    print(i)
'''

## level 2
#list(map(print, list(map(int, map(getattr(0.5, '__add__'), map(getattr(0.4472135954999579, '__mul__'), map(getattr(1.618033988749895, '__pow__'),  map(int, getattr(getattr(open(0), 'read')(), 'split')()))))))))

## level 3

print(list(map(getattr(getattr(',', 'join')(map(str, list(range(1,10001)))), 'replace'), list(range(15, 10001, 15)), getattr(getattr('FizzBuzz ', '__mul__')(666), 'split')())))

#print(getattr(',', 'join')(map(str, list(range(1,10001)))))
#print(list(list(range(15, 10001, 15)))))
