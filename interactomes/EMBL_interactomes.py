'''

This script construct a tissue/cell line specific interactome from a generic interactome 
and expression data of that tissue/cell line from an EMBL experiment dataset. We assume 
that if an interactions is present in the generic interactome and the two interacting 
proteins are expressed in given tissue/cell line, that interaction is also present in
the specific interactome.

INPUT:
- generic_interactome: tab separated file containing generic interactome.
	Format: each line indicates two interacting proteins separated by TAB.
- expression_data: .tsv EMBL expression experiment file, in wich each column
	is a tissue/cell line and each line is the expresion levels of a protein
	in given tissues/cell lines.
- celltype_column: integer indicating the number of the column (tissue/cell-line)
	from wich we want to reconstruct our specific interactome.
	
OUTPUT:
- specific_interactome: tab separated file (same format as the generic interactome)
	containing the list of intteractions specific to our tissue/cell line
	
ASUMPTIONS:
- The expression unit of genes is ________.
- Genes with expression values lower than 0.5 are considered not expresed.
	
'''

import sys
import datetime






weighted = False
for arg in sys.argv:
	if arg.startswith('-'):
		if arg == '-w':
			weighted = True
			sys.argv.remove(arg)

if len(sys.argv) != 4:
	print('\nINVALID ARGUMENTS: python3 EMBL_interactomes.py [-w] generic_interactome expression_data celltype_column(int)\n', file=sys.stderr)
	exit()

if type(int(sys.argv[3])) != int:
	print('\nINVALID ARGUMENT: argument indicating the column number must be an integer\n', file=sys.stderr)
	exit()

f_generic_interactome = sys.argv[1]

f_expresion_data = sys.argv[2]

selcol = int(sys.argv[3])

cutoff = 0.5

d_genes = {}

with open(f_expresion_data, 'r') as expresion_data:
	header = True
	for line in expresion_data:
		if line.startswith('#'):
			continue 
		l_line = line.strip('\n').split('\t')
		if header:
			interactome_name = l_line[selcol]
			header = False
		else:
			gene = l_line[1]
			expresion = l_line[selcol]
			if expresion != '':
				if float(expresion) >= cutoff:
					d_genes[gene] = expresion


#print ('### Expresion data: ', f_expresion_data)
#print ('### Generic interactome: ', f_generic_interactome)
#print ('### Colum: ', selcol, ' (', interactome_name, ')')
#print ('### CutOff: ', cutoff)

print ('### Expresion data: ', f_expresion_data, file = sys.stderr)
print ('### Generic interactome: ', f_generic_interactome, file = sys.stderr)
print ('### Colum: ', selcol, ' (', interactome_name, ')', file = sys.stderr)
print ('### CutOff: ', cutoff, file = sys.stderr)



with open(f_generic_interactome, 'r') as generic_interactome:
	for line in generic_interactome:
		l_line = line.strip('\n').split('\t')
		interaction = True
		expresion_values = []
		for interactor in [l_line[0], l_line[1]]:
			if interactor not in d_genes.keys():
				interaction = False
			else:
				expresion_values.append(float(d_genes[interactor]))
		if interaction:
			if weighted:
				weight = min(expresion_values)
				print("\t".join([l_line[0], l_line[1]]) + '\t' + str(weight))
			else:
				print("\t".join([l_line[0], l_line[1]]))

