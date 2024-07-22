#! /bin/bash

## Read input
in_csv=$1
model=$2
out_csv=$3

## Apply spare test
# cmd="spare_score -a test -i $in_csv -o $out_csv -kv $vkey -t $target -mt SVM -k linear -pg 1"
cmd="spare_score -a test -i $in_csv -m $model -o $out_csv"
echo "About to run: $cmd"
$cmd
