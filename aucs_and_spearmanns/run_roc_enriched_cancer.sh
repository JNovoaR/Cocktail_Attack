#!/bin/bash

### bash xxxxxx.sh sort_seltrg_folder db_descriptions cancer_names f_output

folder=$1
f_db_descriptions=$2
f_synonisms=$3
f_output=$4

params=("DEN" "APL" "NCC" "SLCC" "CC")
possitive_cutoffs=("1" "2" "3")


touch $f_output

for param in ${params[@]}; do
	for cutoff in ${possitive_cutoffs[@]}; do
		for file in `ls $folder`; do
			echo "python3 postprocesing/roc_enriched_cancer.py $folder/$file $f_db_descriptions $f_synonisms $param $cutoff >>$f_output"
			python3 postprocesing/roc_enriched_cancer.py $folder/$file $f_db_descriptions $f_synonisms $param $cutoff >>$f_output
		done
	done
done

echo "REMEMBER!!!! THis script does not rewrite the output file, just add to it (>>)."
