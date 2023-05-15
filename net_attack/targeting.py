import sys
from igraph import *
from igraph import Graph as graph
import copy #esto es necesario?
import datetime
import os

#-w to indicate if the interactomes are weighted
weighted = False                                                                                   
#-h to indicate that interactomes have # headers at the begining of the file
header = False


for argument in sys.argv:
	if argument.startswith('-'):
		if 'h' in argument:
			header = True
		if 'w' in argument:
			weighted = True
		sys.argv.remove(argument)


if header:
	for i in (1, 2):
		if len(sys.argv)==6:
			f_name = sys.argv[i]+'_tmp_'+str(datetime.datetime.now().microsecond) + sys.argv[5]
		else:
			f_name = sys.argv[i]+'_tmp_'+str(datetime.datetime.now().microsecond)
		f = open(f_name, 'w')
		f_og = open(sys.argv[i], 'r')
		for j in f_og:
			if not j.startswith('#'):
				f.write(j)
		f.close()
		f_og.close()
		if i == 1:
			original_healthy=graph.Read_Ncol(f_name, weights=weighted, directed=False)
		elif i == 2:
			original_cancer=graph.Read_Ncol(f_name, weights=weighted, directed=False)
		os.remove(f_name)
else:
	original_healthy=graph.Read_Ncol(sys.argv[1], weights=weighted, directed=False)
	original_cancer=graph.Read_Ncol(sys.argv[2], weights=weighted, directed=False)
	
cocktails_file=open(sys.argv[3], 'r')




if len(sys.argv)==6:
	all_cocktails=False
	first_cocktail=int(sys.argv[4])
	last_cocktail=int(sys.argv[5])
elif len(sys.argv)==4:
	all_cocktails=True
	first_cocktail=0
	last_cocktail=0
else:
	print('Error: Unsupported command line. Enter ([] elements are optionals): ................................', file=sys.stderr)

original_healthy_nodes_list=tuple(original_healthy.vs()["name"])
original_healthy_n_nodes=original_healthy.vcount()
original_healthy_density=original_healthy.density()
original_healthy_average_path_lenght=original_healthy.average_path_length(directed=False)
original_healthy_number_connected_components=len(original_healthy.components())
original_healthy_size_largest_connected_component=original_healthy.components().giant().vcount()
original_healthy_cluster_coficiency=original_healthy.transitivity_undirected(mode="zero")

original_cancer_nodes_list=tuple(original_cancer.vs()["name"])
original_cancer_n_nodes=original_cancer.vcount()
original_cancer_density=original_cancer.density()
original_cancer_average_path_lenght=original_cancer.average_path_length(directed=False)
original_cancer_number_connected_components=len(original_cancer.components())
original_cancer_size_largest_connected_component=original_cancer.components().giant().vcount()
original_cancer_cluster_coficiency=original_cancer.transitivity_undirected(mode="zero")

print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %('Cocktail','Den_Heal_Ratio', 'Den_Cancer_Ratio','APL_Heal_Ratio','APL_Can_Ratio','NCC_Heal_Ratio','NCC_Can_Ratio','SLCC_Heal_Ratio','SLCC_Can_Ratio','Clust.Cof_Heal_Ratio','Clust.Cof_Can_Ratio'))

first_line=True
n='Null' #n tiene que existir antes del bucle teniendo valor distinto a cero.
m=0

for line in cocktails_file:
	if first_line:
		drugs_per_cocktail=len(line.split())-1
		first_line=False
	if line[0]=='>':
		m+=1
		if m in range(first_cocktail,last_cocktail+1) or all_cocktails:
			n=drugs_per_cocktail
			list_line=line.strip('\n').split()
			list_line.pop(0)	#El pop es para quitar el > del principio.
			cocktail=' '.join(list_line)
			disgregated_healthy=copy.deepcopy(original_healthy)
			disgregated_cancer=copy.deepcopy(original_cancer)
			healthy_nodes_list=list(original_healthy_nodes_list)
			cancer_nodes_list=list(original_cancer_nodes_list)
	else:
		if m in range(first_cocktail,last_cocktail) or all_cocktails:
			for target in line.strip('\n').split():
				if target in healthy_nodes_list:
					disgregated_healthy.delete_vertices(target)
					healthy_nodes_list.remove(target)
				if target in cancer_nodes_list:
					disgregated_cancer.delete_vertices(target)
					cancer_nodes_list.remove(target)
			n-=1
	if n==0:
		if disgregated_healthy.vcount()!=original_healthy_n_nodes or disgregated_cancer.vcount()!=original_cancer_n_nodes:
			Den_Heal_Ratio=original_healthy_density/disgregated_healthy.density()
			Den_Can_Ratio=original_cancer_density/disgregated_cancer.density()
			APL_Heal_Ratio=original_healthy_average_path_lenght/disgregated_healthy.average_path_length(directed=False)
			APL_Can_Ratio=original_cancer_average_path_lenght/disgregated_cancer.average_path_length(directed=False)
			NCC_Heal_Ratio=original_healthy_number_connected_components/len(disgregated_healthy.components())
			NCC_Can_Ratio=original_cancer_number_connected_components/len(disgregated_cancer.components())
			SLCC_Heal_Ratio=original_healthy_size_largest_connected_component/disgregated_healthy.components().giant().vcount()
			SLCC_Can_Ratio=original_cancer_size_largest_connected_component/disgregated_cancer.components().giant().vcount()
			Clust_Cof_Heal_Ratio=original_healthy_cluster_coficiency/disgregated_healthy.transitivity_undirected(mode="zero")
			Clust_Cof_Can_Ratio=original_cancer.transitivity_undirected(mode="zero")/disgregated_cancer.transitivity_undirected(mode="zero")
			worth_printing=False
			for value in [APL_Heal_Ratio, APL_Can_Ratio, NCC_Heal_Ratio, NCC_Can_Ratio, SLCC_Heal_Ratio, SLCC_Can_Ratio, Clust_Cof_Heal_Ratio, Clust_Cof_Can_Ratio]:
				if round(value, 3)!=1:
					worth_printing=True
			if worth_printing:
				print('%s\t%.5f\t%.5f\t%.5f\t%.5f\t%.5f\t%.5f\t%.5f\t%.5f\t%.5f\t%.5f' %(cocktail, Den_Heal_Ratio, Den_Can_Ratio, APL_Heal_Ratio, APL_Can_Ratio, NCC_Heal_Ratio, NCC_Can_Ratio, SLCC_Heal_Ratio, SLCC_Can_Ratio, Clust_Cof_Heal_Ratio, Clust_Cof_Can_Ratio))
		print('Cocktail n. '+str(m), end='\r', file=sys.stderr)
	if m>last_cocktail and not all_cocktails:
		break
		
cocktails_file.close()
