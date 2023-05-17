#!/bin/bash

### bash xxxxxx.sh sort_seltrg_folder list_efficacious_co f_output

folder=$1
list_efficacious_co=$2
f_output=$3

params=("DEN" "APL" "NCC" "SLCC" "CC")


touch $f_output

for param in ${params[@]}; do
	for file in `ls $folder`; do
		echo "python3 postprocesing/roc_enriched_synergylab.py $folder/$file $list_efficacious_co $param >>$f_output"
		python3 postprocesing/roc_enriched_synergylab.py $folder/$file $list_efficacious_co $f_synonisms $param >>$f_output
	done
done

echo "REMEMBER!!!! THis script does not rewrite the output file, just add to it (>>)."
