#! /bin/bash -x

in_csv=$1
target=$2
cent_vals=$3
bin_size=$4
out_csv=$5

# Load R module
module load R/4.3

echo "Calculating centiles for: $in_csv"
cmd="Rscript ../../utils/centiles/util_calc_centiles.r -i $in_csv -t $target -o ${out_csv} -c $cent_vals -b $bin_size -v"
echo "About to run: $cmd"
$cmd


