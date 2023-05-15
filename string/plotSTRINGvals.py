import sys
import matplotlib.pyplot as plt


fname = sys.argv[1]

l = []
with open(fname, "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		l.append(int(l_line[2]))

l_cutoffs = []
l_ocurrencies = []

for cutoff in range(0, 1010, 10):
	l_cutoffs.append(cutoff)
	n_ocurrencies = 0
	for i in l:
		if i > cutoff:
			n_ocurrencies += 1
	l_ocurrencies.append(n_ocurrencies)

plt.scatter(l_cutoffs,l_ocurrencies)
plt.savefig('plotSTRINGvals.png')
plt.show()
