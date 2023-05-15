#Este drug combiner acepta targeting files para generar cocktails especificos de cada par de redes pero tambien funciona sin ellos. Ademas tmb toma action files.

import sys

			

if len(sys.argv) < 4:
	print('Invalid arguments: python3 drug_combiner.py drugs_file actions_file drugs_per_cocktail [targeting_file]', file=sys.stderr)
	sys.exit()

mod = False
if len(sys.argv) == 5:
	mod = True
	targeting_drugs_file=open(sys.argv[4], 'r')

try:
	drug_file=open(sys.argv[1], 'r')
except IOError:
	print("Drugs file not found",file=sys.stderr)
	sys.exit()


try:
	n=int(sys.argv[3])
except ValueError:
	print('Drugs per cocktail must be an integer', file=sys.stderr)
	sys.exit()

f_actions=open(sys.argv[2], 'r')
included_actions=[]
for line in f_actions:
	l_line= line.strip().split("\t")
	action = l_line[1]
	if l_line[2] == "F":
		pass
	elif l_line[2] == "T":
		included_actions.append(action)
	else:
		print("WARNING! One of the actions have an assigned value different than T or F", file=sys.stderr)
		print(action, file=sys.stderr)

## Features

ID=5 #Target-ID colum. Esta en 5 para sacar GeneNames de targets_with_genenames // Cambiar por 7 para sacar UniProt de target_with_gennames

App=2 #Approval colum

Action=3 #Action colum

Filter=True #Whether we should remove entire drugs wich at least one of their actions is not included (instead of only removing targets of the drug)

## Reads the targeting drug file.
list_targeting_drugs=[]
if mod:
	for line in targeting_drugs_file:
		list_line=line.split('\t')
		if 'D' in list_line[0]:
			list_targeting_drugs.append(list_line[0])

## Read the drugs file and creates a dictionary drug-targets:
dict_drugs={}
if Filter:
	drugs_to_filter = []
for line in drug_file:
	list_line=line.split('\t')
	if list_line[App]=='True':
		drug_name=list_line[0]
		if list_line[Action] in included_actions:
			if drug_name in list_targeting_drugs or not mod:
				target=list_line[ID]
				if drug_name in dict_drugs.keys():
					dict_drugs[drug_name]+=' '+target.strip()
				else:
					dict_drugs[drug_name]=target.strip()
		else:
			if Filter:
				drugs_to_filter.append(drug_name)
drug_file.close()

## If filter: Filtering drugs wich at least one of their actions is not included
if Filter:
	for drug in drugs_to_filter:
		if drug in dict_drugs.keys():
			del dict_drugs[drug]
				

## Creates all cocktails with an autorrecoursive funtion:
list_drugs=list(dict_drugs.keys())
m=n
counter=0

index_cocktail=[]
p=-1
number_of_drugs=len(list_drugs)
number_of_cocktails=0
def AddOneMoreB(dict_drugs, number_of_drugs, index_cocktail, m, p):
	m-=1
	p+=1
	for i in range(p, number_of_drugs):
		index_cocktail.append(i)
		if m!=0:
			AddOneMoreB(dict_drugs, number_of_drugs, index_cocktail, m, p)
		if len(index_cocktail)==n:
			output_index_cocktail=index_cocktail
			output_cocktail=''
			targets=[]
			cocktail=[]
			for index in output_index_cocktail:
				drug=list_drugs[index]
				cocktail.append(drug)
				targets.append(dict_drugs[drug])
			print("-".join(cocktail), end = "\t")
			print(" ".join(targets))
			global number_of_cocktails
			number_of_cocktails+=1
		index_cocktail.pop()
		p+=1
		if len(index_cocktail)==0:
				global counter
				counter+=1
				print(counter, 'drugs combined', end='\r', file=sys.stderr)			
	

AddOneMoreB(dict_drugs, number_of_drugs, index_cocktail, m, p)


## Prints some data to the user.
print('Done!                        \n', file=sys.stderr)
print(len(list_drugs), ' approved drugs detected', file=sys.stderr)
print(number_of_cocktails, 'cocktails generated\n', file=sys.stderr)
