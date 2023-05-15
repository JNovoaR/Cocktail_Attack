#!/bin/bash

echo "#!/bin/bash"

#echo "#SBATCH -J sbatch_example_opts_in_file"
#echo "#SBATCH -o my_program.output"
#echo "#SBATCH -e my_program.errors"
#echo "#SBATCH --mem=4096"
#echo "#SBATCH --time=0"
#echo "#SBATCH --cpus-per-task=1"


healthy_file=$1
cancer_file=$2
cocktails_file=$3
chunks=$4
output_id=$5

arg=""

if [ $# -eq 6 ]; then
	arg="$6"
	if [[ "$6" == *"w"* ]]; then
		arg_extension="_w_"
	fi
fi

n_cocktails=$(cat $cocktails_file | wc -l)

cocktails_perchunk=$(expr $n_cocktails / $chunks | awk '{print int($1)}')
cocktails_perchunk=$(expr $cocktails_perchunk + 1)


for i in $(seq 1 $chunks); do
	h=$(($i-1)) 
	first_c=$(($cocktails_perchunk * $h))
	last_c=$(( $cocktails_perchunk * $i))
	time_stamp=$(date | tr ' ' '_')
	output_file="temp_$output_id$arg_extension._chunk-$i-$time_stamp"
	err_file="err_$output_id._chunk-$i-$time_stamp"
	echo "Rscript ~/Cocktails/targeting/rtargeting.R $arg $healthy_file $cancer_file $cocktails_file $first_c $last_c >~/Cocktails/targeting/on_use/chunks/$output_file 2>~/Cocktails/targeting/on_use/chunks/err/$err_file &"
	#Rscript rtargeting.R $arg $healthy_file $cancer_file $cocktails_file $first_c $last_c >~/data/targeting_output/$output_file 2>~/data/targeting_output/ERR_targeting/$err_file
done
