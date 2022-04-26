from itertools import product

what = [150, 172, 240, 25, 157, 250, 202, 61, 162, 237, 147, 118, 224, 175, 202, 48, 161, 222, 212, 43,145, 232, 201, 103, 179]
numArray = [154, 43, 63, 200]
k = [0, 0, 0, 0]

# Actual Check
def check(a):
	global level
	num1 = 0
	for i in range(len(a)):
		num1 += a[i] << i
	if numArray[level] == num1:
		num2 = 0
		for i in range(8):
			num2 += a[i] * 3 << i
		num3 = num2 % 256
		k[level] = num3
		level += 1
		if level == 4:
			for i in range(len(what)):
				what[i] ^= k[i % 4]
			print(''.join([chr(c) for c in what]))
		else:
			a = [False for _ in range(8)]

# Brute Force
answer = [None, None, None, None]
all_a = product((False, True), repeat=8)
for a in all_a:
	num1 = 0
	for i in range(len(a)):
		num1 += a[i] << i
	if num1 in numArray:
		print(f'level: {numArray.index(num1)}, a: {a}')
		answer[numArray.index(num1)] = a

level = 0
for a in answer:
	check(a)

