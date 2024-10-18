#! /bin/bash

## Read input
in_csv=$1
vkey=$2
target=$3
out_mdl=$4

## Apply spare train
cmd="spare_score -a train -i $in_csv -o $out_mdl -kv $vkey -t $target -mt SVM -k linear -pg 1"
# cmd="spare_score -a train -i $in_csv -o $out_mdl -kv $vkey -t $target -mt MLP -pg 1"
echo "About to run: $cmd"
$cmd
