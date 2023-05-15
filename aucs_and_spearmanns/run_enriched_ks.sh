#!/bin/bash

### bash xxxxxx.sh sort_seltrg_folder synonims_file ample_size output_file

folder=$1
f_synonims=$2
sample_size=$3
f_output=$4


echo ">$f_output"

for file in `ls $folder`; do
	python3 postprocesing/enriched_ks.py $folder/$file drugbank_parser/on_use/db_descriptions $f_synonims $sample_size >>$f_output
done

