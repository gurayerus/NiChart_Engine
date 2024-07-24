#! /bin/bash

## Read input
in_csv=$1
model=$2
stype=$3
out_csv=$4

## Apply spare test
# cmd="spare_score -a test -i $in_csv -o $out_csv -kv $vkey -t $target -mt SVM -k linear -pg 1"
cmd="spare_score -a test -i $in_csv -m $model -o ${out_csv%.csv}_tmpout.csv"
echo "About to run: $cmd"
$cmd

## Change column name, remove first (index) column
sed "s/SPARE_score/SPARE${stype}/g" ${out_csv%.csv}_tmpout.csv | cut -d, -f2- > $out_csv
rm -rf ${out_csv%.csv}_tmpout.csv
