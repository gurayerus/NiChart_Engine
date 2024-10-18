#! /bin/bash -x

in_csv=$1
cent_vals=$2
bin_size=$3
out_csv=$4

# Load R module
module load R/4.3

## For each column after the first two (in csv format: MRID,Age,Var1,Var2,...)
out_dir=`dirname $out_csv`
out_tmp=${out_dir}/tmp_centiles_singlevar
mkdir -pv ${out_tmp}

for sel_var in `head -1 $in_csv | cut -d, -f3- | sed 's/,/ /g'`; do
    echo "Calculating centiles for: $sel_var"
    cmd="Rscript ../../utils/centiles/util_calc_centiles.r -i $in -o $out -t $var -c $cent -b $bin -v"
    echo "About to run: $cmd"
    $cmd
done


