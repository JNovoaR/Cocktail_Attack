import sys

r_cocktail_file = sys.argv[1]


d_targets_cocktails = {}


with open(r_cocktail_file, "r") as f:
	for line in f:
		l_line = line.strip().split(" ")
		cocktail = l_line[0]
		targets = list(set(l_line[1:]))
		targets.sort()
		targets = " ".join(targets)
		if targets in d_targets_cocktails.keys():
			d_targets_cocktails[targets].append(cocktail)
		else:
			d_targets_cocktails[targets] = [cocktail]

for targets in d_targets_cocktails.keys():
	for cocktails in d_targets_cocktails[targets]:
		print(cocktails + " " + targets)
		
