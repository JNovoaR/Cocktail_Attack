# Script to turn a regular trg output in a trgsel (cinco columnas mas con la selectividad de cada parametro).

import sys

trg_file = sys.argv[1]

with open(trg_file, "r") as f:
	for line in f:
		if "Cocktail" in line:
			continue
		l_line = line.strip().split()
		print(line.strip(), end = "\t")
		sel_list = [str(round(float(l_line[1]) - float(l_line[2]), 5)), str(round(float(l_line[4]) - float(l_line[3]), 5)), str(round(float(l_line[6]) - float(l_line[5]), 5)), str(round(float(l_line[7]) - float(l_line[8]), 5)), str(round(float(l_line[9]) - float(l_line[10]), 5))]
		print("\t".join(sel_list))
