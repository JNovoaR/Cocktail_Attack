#!/bin/bash

### bash xxxxxx.sh trgivi_folder db_descriptions cancer_names f_output

folder=$1
f_db_descriptions=$2
f_synonisms=$3
f_output=$4



touch $f_output


for file in `ls $folder`; do
	echo "python3 postprocesing/roc_enriched_trgivi.py $folder/$file $f_db_descriptions $f_synonisms >>$f_output"
	python3 postprocesing/roc_enriched_trgivi.py $folder/$file $f_db_descriptions $f_synonisms >>$f_output
done


echo "REMEMBER!!!! THis script does not rewrite the output file, just add to it (>>)."
