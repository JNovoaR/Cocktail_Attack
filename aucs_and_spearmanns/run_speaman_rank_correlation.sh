#!/bin/bash

### bash xxxxxx.sh sort_seltrg_folder db_descriptions cancer_names f_output

folder=$1
f_db_descriptions=$2
f_synonisms=$3
f_output=$4

params=("DEN" "APL" "NCC" "SLCC" "CC")


touch $f_output

for param in ${params[@]}; do
	for file in `ls $folder`; do
		echo "python3 postprocesing/speaman_rank_correlation.py $folder/$file $f_db_descriptions $f_synonisms $param >>$f_output"
		python3 postprocesing/speaman_rank_correlation.py $folder/$file $f_db_descriptions $f_synonisms $param >>$f_output
	done
done

echo "REMEMBER!!!! THis script does not rewrite the output file, just add to it (>>)."
