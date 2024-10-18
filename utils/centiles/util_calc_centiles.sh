#! /bin/bash

in_csv=$1
cent=$2
bins=$3
out_dir=$4
out_csv=$5

# Load R module
module load R/4.3

## For each column after the first two (in csv format: MRID,Age,Var1,Var2,...)
out_tmp=${out_dir}/tmp_centiles_singlevar
mkdir -pv ${out_tmp}

for sel_var in `head -1 $in_csv | cut -d, -f3- | sed 's/,/ /g'; do
    echo "Calculating centiles for: $sel_var
    cmd="Rscript ../../utils/centiles/util_calc_centiles.r -i $in -o $out -t $var -c $cent -b $bin -v"
    echo "About to run: $cmd"
    $cmd
