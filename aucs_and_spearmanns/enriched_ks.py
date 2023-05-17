import sys
from statistics import mean
import numpy as np
from scipy import stats
from scipy.stats import kstest
import matplotlib.pyplot as plt
###python3 xxxx.py sorted_cocktails db_descriptions terms_to_search sample_size

f_sorted_cocktails = sys.argv[1]
f_db_descriptions = sys.argv[2]
f_terms_to_search = sys.argv[3]
sample_size = int(sys.argv[4])

d_descriptions = {}
with open(f_db_descriptions, "r") as f:
	for line in f:
			l_line = line.strip().split("\t")
			d_descriptions[l_line[0]] = " ".join([l_line[1].lower(), l_line[2].lower(), l_line[3].lower()])

	

def read_cofile (cofile):
	co_list = []
	with open(cofile, "r") as f:
		for line in f:
			if not line.startswith("Cocktail"):
				l_line = line.strip().split("\t")
				co = l_line[0]
				if co != "":
					co_list.append(co)
	return(co_list)



co_random = read_cofile(f_sorted_cocktails)
co_biassed = co_random[0:sample_size]

terms_to_search = read_cofile(f_terms_to_search)


l_n_matched_per_co_biassed = []
for co in co_biassed:
	drugs = co.split("-")
	matches = 0
	for drug in drugs:
		descr = d_descriptions[drug]
		match = False
		for term in terms_to_search:
			if term in descr:
				match = True
		if match:
			matches += 1
	l_n_matched_per_co_biassed.append(matches)

mean_matches_biassed = mean(l_n_matched_per_co_biassed)


l_n_matched_per_co_random = []
for co in co_random:
	drugs = co.split("-")
	matches = 0
	for drug in drugs:
		descr = d_descriptions[drug]
		match = False
		for term in terms_to_search:
			if term in descr:
				match = True
		if match:
			matches += 1
	l_n_matched_per_co_random.append(matches)

mean_matches_random = mean(l_n_matched_per_co_random)

ks_test = stats.kstest(l_n_matched_per_co_biassed,l_n_matched_per_co_random)
pvalue = ks_test[1]
diff = mean_matches_biassed - mean_matches_random


print(l_n_matched_per_co_random)
plt.plot(range(0, len(l_n_matched_per_co_random)), l_n_matched_per_co_random, "o", color='black')
#plt.plot(range(0, 1000), l_n_matched_per_co_random[0:1000], "o", color='black')
plt.savefig('plot.png')
#print("\t".join([f_sorted_cocktails, str(round(mean_matches_biassed, 5)), str(round(mean_matches_random, 5)), str(round(diff, 5)), str(pvalue)]))






