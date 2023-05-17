import sys
from scipy.stats import chisquare
from statistics import mean
import numpy as np
from scipy import stats
from scipy.stats import kstest
import matplotlib.pyplot as plt
import roc_utils as ru
from sklearn import metrics

f_top50 = sys.argv[1]
f_trgivi = sys.argv[2]
f_db_descriptions = sys.argv[3]
f_terms_to_search = sys.argv[4]




possitive_cutoff = 1
param_col = 3






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
	return(co_list)

l_costop50 = read_cofile(f_top50, param_col)
l_costrgivi = read_cofile(f_trgivi, param_col)

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




l_n_matched_top50 = []

for co in l_costop50:
	drugs = co.split("-")
	matches = 0
	for drug in drugs:
		descr = d_descriptions[drug]
		match = False
		for term in terms_to_search:
			if term.lower() in descr:
				match = True
		if match:
			matches += 1
	l_n_matched_top50.append(matches)


labels_top50 = []

for matches in l_n_matched_top50:
	if matches >= possitive_cutoff:
		labels_top50.append(1)
	else:
		labels_top50.append(0)

l_n_matched_trgivi = []

for co in l_costrgivi:
	drugs = co.split("-")
	matches = 0
	for drug in drugs:
		descr = d_descriptions[drug]
		match = False
		for term in terms_to_search:
			if term.lower() in descr:
				match = True
		if match:
			matches += 1
	l_n_matched_trgivi.append(matches)


labels_trgivi = []

for matches in l_n_matched_trgivi:
	if matches >= possitive_cutoff:
		labels_trgivi.append(1)
	else:
		labels_trgivi.append(0)

real_1s = labels_top50.count(1)
real_0s = labels_top50.count(0)



expected_1s = (labels_trgivi.count(1) / len(labels_trgivi)) * len(labels_top50)
expected_0s = (labels_trgivi.count(0) / len(labels_trgivi)) * len(labels_top50)

print(real_1s,real_0s,"|",expected_1s,expected_0s)

print(chisquare([real_1s, real_0s], f_exp=[expected_1s, expected_0s]))
 
