#! /bin/bash -x

in_csv=$1
target=$2
cent_vals=$3
bin_size=$4
out_csv=$5

# Load R module
module load R/4.3

if [ `head -1 $in_csv | grep $target | wc -l` == '0' ]; then
    echo 'ROI missing in csv file, skipping: $target'
    echo '"VarName","Age","centile_5","centile_25","centile_50","centile_75","centile_95"' > $out_csv

else
    echo "Calculating centiles for: $in_csv"
    cmd="Rscript ../../utils/centiles/util_calc_centiles.r -i $in_csv -t $target -o ${out_csv} -c $cent_vals -b $bin_size -v"
    echo "About to run: $cmd"
    $cmd
fi


