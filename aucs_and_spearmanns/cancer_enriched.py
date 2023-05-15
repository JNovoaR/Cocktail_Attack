import sys

d_descriptions = {}
with open(sys.argv[3], "r") as f:
	for line in f:
			l_line = line.strip().split("\t")
			d_descriptions[l_line[0]] = " ".join([l_line[1], l_line[2], l_line[3]])

	

def read_cofile (cofile):
	drugs_list = []
	with open(cofile, "r") as f:
		for line in f:
			l_line = line.strip().split("\t")
			drugs = l_line[0].split("-")
			drugs_list = drugs_list + drugs
	return(drugs_list)

drugs_enriched = read_cofile(sys.argv[1])
drugs_random = read_cofile(sys.argv[2])

terms_to_search = read_cofile(sys.argv[3])

count_enriched = 0
size_enriched = len(drugs_enriched)
for drug in drugs_enriched:
	descr = d_descriptions[drug]
	match = False
	for term in terms_to_search:
		if term in descr:
			match = True
	if match:
		count_enriched += 1

count_random = 0
size_random = len(drugs_random)
for drug in drugs_random:
	descr = d_descriptions[drug]
	match = False
	for term in terms_to_search:
		if term in descr:
			match = True
	if match:
		count_random += 1
		
		

print(count_enriched)
print(size_enriched)
print()
print(count_random)
print(size_random)

