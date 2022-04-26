morse_file = 'magically_recovered/M7wfU5hzUELR'

with open(morse_file, 'r') as f:
	morse = f.read()

print(morse.replace('_', '-'))
