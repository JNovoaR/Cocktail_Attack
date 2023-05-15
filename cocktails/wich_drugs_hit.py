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

dco = {}
for line in cocktails:
	l_line = line.strip().split("\t")
	cocktail = l_line[0]
	targets = l_line[1].strip().split(" ")
	hit = False
	for i in targets:
		if i in d.keys():
			hit = True
				
	if hit:
		dco[cocktail] = ""

print(dco.keys())

for i in dco.keys():
	print(i)

print("HITS:", str(len(dco.keys())), file = sys.stderr)
		
