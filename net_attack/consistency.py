import sys


targeting_file = open(sys.argv[1], 'r')

params= ("DEN", "APL", "NCC", "SLCC", "CC")
pol = (">","<","<",">",">") #what is better in cancer?

d={}
for line in targeting_file:
	if line.startswith("D"):
		l_line = line.strip('\n').split('\t')
		cocktail = l_line[0]
		v_den = (l_line[1], l_line[2])
		v_apl = (l_line[3], l_line[4])
		v_ncc = (l_line[5], l_line[6])
		v_slcc = (l_line[7], l_line[8])
		v_cc = (l_line[9], l_line[10])
		n = 0
		d[cocktail] = []
		for v in (v_den, v_apl, v_ncc, v_slcc, v_cc):
			diff = float(v[0]) - float(v[1])
			if pol[n] == ">":
				if diff >= 0:
					good = False
				else:
					good = True
			elif pol[n] == "<":
				if diff <= 0:
					good = False
				else:
					good = True
			else:
				print("ERROR! Bad pol value:", pol[n])
			d[cocktail].append(good)
			n +=1

n_cocktails = len(d.keys())
unit_ratio = 1/n_cocktails


matrix = []
for i in params:
	row=[]
	for i in params:
		row.append(0)
	matrix.append(row)

individual_counts = [0, 0, 0, 0, 0]

for cocktail in d.keys():
	values = d[cocktail]
	n = 0
	for i in d[cocktail]:
		if i:
			individual_counts[n] += unit_ratio
		n+=1	
	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[row])):
			if values[row] == values[col]:
				matrix[row][col] += unit_ratio

how_many_trues = [0, 0, 0, 0, 0, 0]
for i in d.keys():
	print(i + "\t" + "\t".join(map(str, d[i])))
	n = 0
	for j in d[i]:
		if j:
			n+=1
	how_many_trues[n] += unit_ratio 
		

print("", file = sys.stderr)
print("--Ratio good-cocktail/all-cocktail for each parameter--", file = sys.stderr)
print("", file = sys.stderr)

print("\t".join(params), file = sys.stderr)
rounded_ind_counts = [ round(elem, 2) for elem in individual_counts ]
print("\t".join(map(str, rounded_ind_counts)), file = sys.stderr)
print("", file = sys.stderr)
print("--Ratio of coincidence for each pair of parametres--", file = sys.stderr)
print("", file = sys.stderr)
print("*"+"\t"+"\t".join(params), file = sys.stderr)


for i in range(0, len(matrix)):
	rounded_row = [ round(elem, 2) for elem in matrix[i] ]
	print (params[i] + "\t" + "\t".join(map(str, rounded_row)), file = sys.stderr)

print("", file = sys.stderr)
print("--How many cocktails have n trues--", file = sys.stderr)
print("", file = sys.stderr)
rounded_trues = [ round(elem, 2) for elem in how_many_trues ]	
print("0T	1T	2T	3T	4T	5T", file = sys.stderr)
print("\t".join(map(str, rounded_trues)), file = sys.stderr)

		


	
		
