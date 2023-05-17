import sys
from statistics import mean
import numpy as np
from scipy import stats
from scipy.stats import kstest
import matplotlib.pyplot as plt
#import roc_utils as ru
from sklearn import metrics
###python3 xxxx.py sorted_cocktails list_efficacious_co param_name


f_cocktails = sys.argv[1]
f_efficacious_co = sys.argv[2]
param_name = sys.argv[3]
possitive_cutoff = 1


d_params = {
"DEN": 1,
"APL": 2,
"NCC": 3,
"SLCC": 4,
"CC": 5,
}

param_col = d_params[param_name]






	

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

def read_names_file (f_efficacious_co):
	co_list = []
	with open(f_efficacious_co, "r") as f:
		for line in f:
			if not line.startswith("Cocktail"):
				l_line = line.strip().split("\t")
				co = l_line[0]
				antico = "-".join([co.split("-")[1], co.split("-")[0]])
				if co != "":
					co_list.append(co)
					co_list.append(antico)
	return(co_list)


efficacious_cos = read_names_file(f_efficacious_co)




labels = []

for co in l_cos:
	match = False
	possitive = 0
	for effco in efficacious_cos:
		if effco == co:
			match = True
		if match:
			possitive = 1
	labels.append(possitive)


# Compute the ROC curve...
pos_label = True
#roc = ru.compute_roc(X=param_list, y=labels, pos_label=pos_label)
auc = metrics.roc_auc_score(labels, param_list)

file_name = f_cocktails.split("/")[-1]

print(file_name, param_name, auc, sep = "\t")
# ...and visualize it
#ru.plot_roc(roc, label="Sample data", color="red")
#plt.show()








