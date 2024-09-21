#! /bin/bash

## Read input
in_csv=$1
in_mdl=$2
out_csv=$3

## Apply combat learn
out_tmp=${out_csv%.csv}_tmp.csv
cmd="neuroharm -a apply -i $in_csv -m $in_mdl -u $out_tmp"
echo "About to run: $cmd"
$cmd

## Remove suffix
rm_suff='_HARM'
cmd="python ../../utils/generic/util_remove_suffix.py $out_tmp $rm_suff $out_csv"
echo "About to run: $cmd"
$cmd
rm -rf ${out_tmp}
