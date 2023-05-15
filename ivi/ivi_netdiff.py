import sys

healthy_ivi_file = sys.argv[1]

cancer_ivi_file = sys.argv[2]



d_ivi = {}
with open(healthy_ivi_file, "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		d_ivi[l_line[0]] = [float(l_line[1]), 0]

with open(cancer_ivi_file, "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		if l_line[0] in d_ivi.keys():
			d_ivi[l_line[0]][1] = float(l_line[1])
		else:
			d_ivi[l_line[0]] = [0, float(l_line[1])]

for node in d_ivi.keys():
	diff = d_ivi[node][1] - d_ivi[node][0]
	print(node + "\t" + str(d_ivi[node][0]) + "\t" + str(d_ivi[node][1]) + "\t" + str(diff))
