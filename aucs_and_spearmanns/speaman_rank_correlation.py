import sys
from statistics import mean
import numpy as np
from scipy import stats
from scipy.stats import kstest
import matplotlib.pyplot as plt
#import roc_utils as ru
from sklearn import metrics
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
###python3 xxxx.py cocktails db_descriptions terms_to_search param_name


f_cocktails = sys.argv[1]
f_db_descriptions = sys.argv[2]
f_terms_to_search = sys.argv[3]
param_name = sys.argv[4]



d_params = {
"DEN": 1,
"APL": 2,
"NCC": 3,
"SLCC": 4,
"CC": 5,
}

param_col = d_params[param_name]






d_descriptions = {}
with open(f_db_descriptions, "r") as f:
	for line in f:
			l_line = line.strip().split("\t")
			d_descriptions[l_line[0]] = " ".join([l_line[1].lower(), l_line[2].lower(), l_line[3].lower()])

	

def read_cofile (cofile, param_col):
	co_list = []
	param_list = []
	with open(cofile, "r") as f:
		for line in f:
			if not line.startswith("Cocktail"):
				l_line = line.strip().split("\t")
				co = l_line[0]
				if co != "":
					co_list.append(co)
					param_list.append(float(l_line[param_col]))
	return(co_list, param_list)

l_cos, param_list = read_cofile(f_cocktails, param_col)

def read_names_file (names_file):
	co_list = []
	with open(names_file, "r") as f:
		for line in f:
			if not line.startswith("Cocktail"):
				l_line = line.strip().split("\t")
				co = l_line[0]
				if co != "":
					co_list.append(co)
	return(co_list)


terms_to_search = read_names_file(f_terms_to_search)




l_n_matched_per_co = []

for co in l_cos:
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
	l_n_matched_per_co.append(matches)



rho, p = spearmanr(param_list, l_n_matched_per_co)

file_name = f_cocktails.split("/")[-1]

plt.scatter(param_list, l_n_matched_per_co)
plt.show()

print(file_name, param_name, rho, p, sep = "\t")

