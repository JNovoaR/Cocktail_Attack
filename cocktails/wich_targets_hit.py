import sys

int1 = open (sys.argv[1], "r")
int2 = open (sys.argv[2], "r")
cocktails = open (sys.argv[3], "r")


d = {}
for f in (int1, int2):
	for line in f:
		l_line = line.strip().split("\t")
		d[l_line[0]] = ""
		d[l_line[1]] = ""

dtrg = {}
for line in cocktails:
	l_line = line.strip().split(" ")
	col1 = True
	for i in l_line:
		if col1:
			cocktail = i
			col1 = False
		else:
			if i in d.keys():
				dtrg[i] = ""

for i in dtrg.keys():
	print(i)

print("TARGET HITS:", str(len(dtrg.keys())), file = sys.stderr)
		
