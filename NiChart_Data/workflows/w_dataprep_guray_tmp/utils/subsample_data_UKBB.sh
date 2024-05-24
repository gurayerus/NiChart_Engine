#! /bin/bash

## This script selects subsamples from data (used for UKBB)

in_csv1=$1
in_csv2=$2
in_csv3=$3
out_csv1=$4
out_csv2=$5
out_csv3=$6
num_sample=$7
key_var=$8
key_uniq=$9

ref_csv=${out_csv1%.csv}_tmp.csv

## Select sample
python ./utils/util_subsample_data.py -i $in_csv1 -n $num_sample -s $key_var -d $key_uniq -o $ref_csv
python util_filter_to_subsampled.py -i $in_csv1 -r $ref_csv -k $key_var -o $out_csv1
python util_filter_to_subsampled.py -i $in_csv2 -r $ref_csv -k $key_var -o $out_csv2
python util_filter_to_subsampled.py -i $in_csv3 -r $ref_csv -k $key_var -o $out_csv3

