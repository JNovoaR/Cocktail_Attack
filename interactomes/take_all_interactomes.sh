#!/bin/bash

if [ $# -eq 0 ]; then
	echo "bash take_all_interactomes.sh generic_interactome expresion_file output_folder file_name_prefix(hw/cw) source_prefix(IBM/CCLE) generic_interactome_prefix(NGI3/STR400/SRT700/ETC) [-w]"
fi


generic_interactome=$1
data_file=$2
folder=$3
prefix=$4
source=$5
cutoff="0.5"
generic_interactome_extension=$6 #before it was NGI3

arg=""
if [ $# -eq 7 ]; then
	arg=" $7"
	arg_extension=$(echo $4 | tr '-' '_')
fi

header=$(grep "Gene ID" $data_file)

keepgoin=true
n=2

mkdir $folder

while $keepgoing; do
	((m=n+1))
	col=$(cut -f$m <<< $header)
	col=$(echo $col | tr ' ' '_' | tr '/' '-' )
	x=$(echo $col | wc -c)
	if [ $x -eq 1 ]; then
		keepgoing=false
	else
		file_name="$folder/$prefix-$col-$source-$generic_interactome_extension-$cutoff.tab"
		python3 /home/jnovoa/Cocktails/interactomes/EMBL_interactomes.py $arg $generic_interactome $data_file $n >$file_name
	fi
	((n=n+1))
done

	
