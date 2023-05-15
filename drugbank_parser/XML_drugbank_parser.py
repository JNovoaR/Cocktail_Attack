import xml.etree.ElementTree as ET
import sys
import re

if len(sys.argv)<3:
	print("Invalid arguments: python3 XML_parsing.py file.xml organism\n(enter 'all' for all targets, enter 'human' for human targets only, etc).",file=sys.stderr)
	sys.exit()
organism=sys.argv[2]

print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %('DrugID','DrugName','Approval','Action','TargetName','GeneName','GenBankProtein','UniProtKB'))

first_drug_name=True
first_drug_id=True
first_action=True
in_target=False
first_target_name=True
in_GB_protein=False
in_uniprot=False
asked_target=True
n=0

drug_id='Null'
drug_name='Null'
approved='Null'
action='Null'
target_name='Null'
GB_protein='Null'
uniprot='Null'
gene_name='Null'

for event, element in ET.iterparse(sys.argv[1],events=("start", "end")):
	if element.tag=='{http://www.drugbank.ca}drug':
		if event=='start':
			n+=1
		elif event=='end':
			n-=1
			if n==0:
				first_drug_name=True
				first_drug_id=True
				first_action=True
				drug_id='Null'
				drug_name='Null'
				approved='Null'
	elif element.tag=='{http://www.drugbank.ca}drugbank-id' and first_drug_id:
		drug_id=element.text
		first_drug_id=False
	elif element.tag=='{http://www.drugbank.ca}name' and first_drug_name:
		drug_name=element.text
		first_drug_name=False
	elif element.tag=='{http://www.drugbank.ca}group':
		# Since when multiple group tags, approved is always the first if present,
		# this considers approved=True when approved is present, except if
		# withdrawn appears later. Other groups dont go against approved.
		if element.text=='approved':
			approved=True
		elif element.text=='withdrawn':
			approved=False
		else:
			if approved == "Null":
				approved = False
	elif element.tag=='{http://www.drugbank.ca}target' and event=='start':
		in_target=True
	elif element.tag=='{http://www.drugbank.ca}organism' and organism!='all':
		if organism==element.text:
			asked_target=True
		elif element.text!=None:
			asked_target=True
		else:
			asked_target=False
			in_target=False		
	elif element.tag=='{http://www.drugbank.ca}action' and in_target:
		action=element.text
	elif element.tag=='{http://www.drugbank.ca}name' and in_target and first_target_name:
		target_name=element.text
		first_target_name=False
	elif element.tag=='{http://www.drugbank.ca}resource'and in_target:
		if element.text=='GenBank Protein Database':
			in_GB_protein=True
		if element.text=='UniProtKB':
			in_uniprot=True
	elif element.tag=='{http://www.drugbank.ca}identifier' and in_GB_protein:
		GB_protein=element.text
		in_GB_protein=False
	elif element.tag=='{http://www.drugbank.ca}identifier' and in_uniprot:
		uniprot=element.text
		in_uniprot=False
	elif element.tag=='{http://www.drugbank.ca}gene-name' and in_target:
		gene_name=element.text
	elif element.tag=='{http://www.drugbank.ca}target' and event=='end' and asked_target:
		print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %(drug_id,drug_name,approved,action,target_name,gene_name,GB_protein,uniprot))
		action='Null'
		target_name='Null'
		GB_protein='Null'
		uniprot='Null'
		in_target=False
		first_target_name=True
		

		
	
