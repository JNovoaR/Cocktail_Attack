import sys

string_main_file = sys.argv[1]##### PONER AQUI LOS NOMBRES DE LOS ARCHIVOS
string_maping_file = sys.argv[2]

with open(string_maping_file, "r") as f:
	d_eq = {}
	for line in f:
		l_line = line.strip().split("\t")
		d_eq[l_line[0]] = l_line[1]


with open(string_main_file, "r") as f:
	header = True
	for line in f:
		if header:
			header = False
			continue
		l_line = line.strip().split(" ")
		new_line = d_eq[l_line[0]] + "\t" + d_eq[l_line[1]] + "\t" + l_line[2]
		print(new_line)



