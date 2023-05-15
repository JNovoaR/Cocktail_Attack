import sys

r_cocktail_file = sys.argv[1]

targets_hit_file = sys.argv[2]

d_hits = {}

with open(targets_hit_file, "r") as f:
	for line in f:
		hit = line.strip()
		d_hits[hit] = ""

with open(r_cocktail_file, "r") as f:
	for line in f:
		l_line = line.strip().split(" ")
		cocktail = l_line[0]
		targets = list(set(l_line[1:]))
		included_targets = []
		for target in targets:
			if target in d_hits.keys():
				included_targets.append(target)
		if len(included_targets) != 0:
			print(cocktail + " " + " ".join(included_targets))

