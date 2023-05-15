import sys

f = open(sys.argv[1], 'r')

for line in f:
	if line.startswith('>'):
		n=1
	if n == 1:
		l_line= line.strip('\n').split(' ')
		c_size= len(l_line)
		l_line.pop(0)
		c= '-'.join(l_line[-c_size+1:])
		print(c, end= ' ')
	if n != 1:
		if n != c_size:
			print(line.strip(), end= ' ')
		else:
			print(line.strip())
	n+=1

