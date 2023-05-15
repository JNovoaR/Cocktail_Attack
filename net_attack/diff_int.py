import sys


f_healthy=sys.argv[1]

f_cancer=sys.argv[2]

d={}
with open(f_healthy, 'r') as healthy:
	for line in healthy:
		if '#' in line:
			continue
		else:
			l_line=line.strip('\n').split('\t')
			interaction = l_line[0]+'\t'+l_line[1]
			d[interaction]='h'	
	
with open(f_cancer, 'r') as cancer:
	for line in cancer:
		if '#' in line:
			continue
		else:
			l_line=line.strip('\n').split('\t')
			interaction = l_line[0]+'\t'+l_line[1]
			if interaction in d.keys():
				d[interaction]='b'
			else:
				d[interaction]='c'
print("node1	node2	type")

for interaction in d.keys():
	print(interaction + '\t' + d[interaction])
