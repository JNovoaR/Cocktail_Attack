import sys

healthy_ci_file = sys.argv[1]

cancer_ci_file = sys.argv[2]

cocktails_file = sys.argv[3]


d_ci = {}
with open(healthy_ci_file, "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		d_ci[l_line[0]] = [float(l_line[1]), 0]

with open(cancer_ci_file, "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		if l_line[0] in d_ci.keys():
			d_ci[l_line[0]][1] = float(l_line[1])
		else:
			d_ci[l_line[0]] = [0, float(l_line[1])]

with open(cocktails_file, "r") as f:
	n = 0
	for line in f:
		healthy_score = 0
		cancer_score = 0
		l_line = line.strip().split("\t")
		cocktail = l_line[0]
		targets = l_line[1:]
		for target in targets:
			if target in d_ci.keys():
				healthy_score += d_ci[target][0]#COULD BE PRODUCT INSTEAD OF SUM
				cancer_score += d_ci[target][1]
		diff_score = cancer_score - healthy_score
		if diff_score != 0:
			print(cocktail + "\t" + str(healthy_score) + "\t" + str(cancer_score) + "\t" + str(diff_score))
		n += 1
		print("Cocktail nº", str(n), end = "\r", file = sys.stderr)
		

