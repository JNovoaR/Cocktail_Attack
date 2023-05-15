import sys

#python3 xxxx.py DRUG_COMBINATION.txt(synergylab) COMPONENTS.txt(synergylab) DC_TO_DCU.txt(synergylab) DC_USAGE.txt(synergylab) db_cas_ids(drugbank)


#some Drug Combinations are gonna be lost due not having drugbank equivalent (or not included between our pool of drugs (inhibitors, etc))

print("\t".join(["DC_ID","DCC_IDs","DRUGBANK_IDs","DCU_ID","DISEASE","EFFICACY","EFFECT_TYPE","TOXICITY","OVERALL"]))

d_cas2db = {}
with open(sys.argv[5], "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		d_cas2db[l_line[1]] = l_line[0]

print(d_cas2db)

d_dcc2cas = {}
with open(sys.argv[2], "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		if ":" in l_line[2]:#handle "CAS:NNN-NNN-NN" formated ids
			d_dcc2cas[l_line[0]] = l_line[2].split(":")[1]
		else:#handle "Null" formated ids
			d_dcc2cas[l_line[0]] = l_line[2]

d_dc2dcu = {}
with open(sys.argv[3], "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		d_dc2dcu[l_line[0]] = l_line[1]

#print(d_dc2dcu)

d_dcu_data = {}
with open(sys.argv[4], "r") as f:
	for line in f:
		l_line = line.strip().split("\t")
		d_dcu_data[l_line[0]] = [l_line[3], l_line[4], l_line[5], l_line[11], l_line[12]]

first_line = True
with open(sys.argv[1], "r") as f:
	for line in f:
		if first_line:
			first_line = False
		else:
			skip_this_dc = False
			l_line = line.strip().split("\t")
			#get dcu (usage) data
			try:#gonna skip if there is not a DCU for this DC
				dcu_id = d_dc2dcu[l_line[0]]
			except KeyError:
				skip_this_dc = True
			dcu_data = d_dcu_data[dcu_id]
			#get dc-db conversion
			l_dccs = l_line[4].split("/")
			l_dbs = []
			for dcc in l_dccs:
				try:#gonna skip if we dont find a drugbank equivalent for one of the drugs
					l_dbs.append(d_cas2db[d_dcc2cas[dcc]])
				except KeyError:
					skip_this_dc = True
			if not skip_this_dc:
				db = "-".join(l_dbs)
				#output
				print("\t".join([l_line[0],l_line[4],db,l_line[3],dcu_id,dcu_data[0],dcu_data[1],dcu_data[2],dcu_data[3],dcu_data[4]]))
			
			
