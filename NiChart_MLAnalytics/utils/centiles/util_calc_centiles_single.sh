#! /bin/bash

in=$1
var=$2
cent=$3
bin=$4
out=$5

cmd="Rscript ../../utils/centiles/util_calc_centiles.r -i $in -o $out -t $var -c $cent -b $bin -v"
echo "About to run: $cmd"
$cmd
