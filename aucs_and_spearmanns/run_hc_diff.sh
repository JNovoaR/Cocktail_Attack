#!/bin/bash

### bash xxxxxx.sh trg_folder output_folder

trg_folder=$1
output_folder=$2

for file in `ls $trg_folder`; do
	if [ "$file" != "chunks" ]; then
	   	python3 postprocesing/hc_diff.py $trg_folder$file >$output_folder/sel$file
	fi
done

