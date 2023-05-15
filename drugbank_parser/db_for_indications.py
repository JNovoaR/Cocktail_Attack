import sys


first_entry = True
new_drug = False
new_description = False
new_indication = False
new_pharmacodynamics = False

drug_id = "Null"
description = "Null"
indication = "Null"
pharmacodynamics = "Null"



with open(sys.argv[1], "r") as f:
	for line in f:
		line = line.strip()
		if line.startswith("<drug type"):
			new_drug = True
			new_description = True
			new_indication = True
			new_pharmacodynamics = True
			if not first_entry:
				print("\t".join([drug_id,description,indication,pharmacodynamics]))	
				drug_id = "Null"
				description = "Null"
				indication = "Null"
				pharmacodynamics = "Null"				
			else:
				first_entry = False
		if new_drug:
			if line.startswith("<drugbank-id primary"):
				drug_id = line.split(">")[1].split("<")[0]
				new_drug = False
		if new_description:
			if line.startswith("<description>"):
				description = line.split(">")[1].split("<")[0]
				new_description = False
		if new_indication:
			if line.startswith("<indication>"):
				indication = line.split(">")[1].split("<")[0]
				new_indication = False	
		if new_pharmacodynamics:
			if line.startswith("<pharmacodynamics>"):
				pharmacodynamics = line.split(">")[1].split("<")[0]
				new_pharmacodynamics = False

print("\t".join([drug_id,description,indication,pharmacodynamics]))
