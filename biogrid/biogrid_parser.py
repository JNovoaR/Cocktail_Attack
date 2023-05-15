#This is like TAB2_parser.py but actually working.
#It parses TAB3 biogrid human database to obtain an undir interactome in format:
#A	B
#A	C
#C	D
#
#CURRENT FILTERS: -Only physical interactions (13th col)
#			-Only human human (id:9606) interactions (16th & 17th col)
#			-Avoid AB AB an also AB BA ones (undirected)


import sys

if sys.argv != 4:
	print("python3 biogrid_parser.py biogrid_file.TAB3 col1 col2")

tab_file = open(sys.argv[1], 'r')

col1 = int(sys.argv[2])

col2 = int(sys.argv[3])

header = True

d = {}
for line in tab_file:
	if header:
		header = False
		continue
	l_line = line.strip().split('\t')
	interaction = [l_line[col1], l_line[col2]]
	interaction.sort() #To avoid A-B / A-B and also A-B / B-A redundancies we just sort 
				#alphabetical and store as a dict key
	interaction = "\t".join(interaction)
	if l_line[12] == "physical":
		if l_line[15] == "9606":
			if l_line[16] == "9606":
				d[interaction] = ""

for i in d.keys():
	print(i)

