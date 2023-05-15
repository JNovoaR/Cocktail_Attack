#!/bin/bash

cocktail_file=$1

time_stamp=$(date | tr ' ' '_')

tmp_file="tmp_cocktail_sorter-$time_stamp"

paste <(cut -f2 $cocktail_file) <(cut -f1 $cocktail_file) | sort >$tmp_file


paste <(cut -f2 $tmp_file) <(cut -f1 $tmp_file)

rm $tmp_file
