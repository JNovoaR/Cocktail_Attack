import sys



params= ("DEN", "APL", "NCC", "SLCC", "CC")
pol = (">","<","<",">",">") #what is better in cancer?

print("Cocktail\tDEN_sel\tAPL_sel\tNCC_sel\tSLCC_sel\tCC_sel")

with open(sys.argv[1], "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		if line.startswith("Cocktail"):
			continue
		v_den = (float(l_line[1]), float(l_line[2]))
		v_apl = (float(l_line[3]), float(l_line[4]))
		v_ncc = (float(l_line[5]), float(l_line[6]))
		v_slcc = (float(l_line[7]), float(l_line[8]))
		v_cc = (float(l_line[9]), float(l_line[10]))
		l_v = [v_den,v_apl,v_ncc,v_slcc,v_cc]
		l_selectivness = ["null","null","null","null","null"]
		for i in range(0, len(params)):
			if pol[i] == ">":
				l_selectivness[i] = str(round(l_v[i][1] / l_v[i][0], 7))
			elif pol[i] == "<":
				l_selectivness[i] = str(round(l_v[i][0] / l_v[i][1], 7))
		print(l_line[0] + "\t" + "\t".join(l_selectivness))
				
