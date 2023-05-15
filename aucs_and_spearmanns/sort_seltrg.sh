#!/bin/bash
### bash xxxxxx.sh seltrg_folder output_folder


seltrg_folder=$1
output_folder=$2

# Create a list with the words "DEN" "APL" "NCC" "SLCC" and "CC"
list=("DEN" "APL" "NCC" "SLCC" "CC")

for file in `ls $seltrg_folder`; do 
	# Loop through each parameter
	for index in "${!list[@]}"
	do
	    element=${list[index]}
	    col=$((index+2))
	    cat $seltrg_folder/$file | grep -v "Cocktail" | sort -rnk $col >$output_folder/sortby$element\_$file
	done
done
