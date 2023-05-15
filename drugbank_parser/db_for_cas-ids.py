import sys


first_entry = True
new_drug = False
new_cas_id = False

drug_id = "Null"
cas_id = "Null"

with open(sys.argv[1], "r") as f:
	for line in f:
		line = line.strip()
		if line.startswith("<drug type"):
			new_drug = True
			new_cas_id = True
			if not first_entry:
				print("\t".join([drug_id,cas_id]))
				drug_id = "Null"
				cas_id = "Null"
			else:
				first_entry = False	
		if new_drug:
			if line.startswith("<drugbank-id primary"):
				drug_id = line.split(">")[1].split("<")[0]
				new_drug = False
		if new_cas_id:
			if line.startswith("<cas-number>"):
				cas_id = line.split(">")[1].split("<")[0]
				new_cas_id = False	
					

print("\t".join([drug_id,cas_id]))			
				
				
				
