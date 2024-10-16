#! /bin/bash

## Read input
in_csv=$1
batch=$2
vkey=$3
vnum=$4
vcat=$5
vspline=$6
out_mdl=$7
out_csv=$8

# ## Apply combat learn
# cmd="neuroharm -a learn -i $in_csv -k $vkey -b $batch -n $vnum -c $vcat -s $vspline -o $out_mdl -u $out_csv"
# echo "About to run: $cmd"
# $cmd


### FIXME : skip -s for now

## Apply combat learn
cmd="neuroharm -a learn -i $in_csv -k $vkey -b $batch -n $vnum -c $vcat -n $vspline -o $out_mdl -u $out_csv"
echo "About to run: $cmd"
$cmd
