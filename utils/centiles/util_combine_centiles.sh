#! /bin/bash +x

## Function to combine individual centile files for each target variable
##  - Discards the header from all files, except the first one

## Read out_file and first input_file
fout=$1
fin1=$2

## Shift args to other input_files
shift;
shift;

## Write first file to output
cat $fin1 > $fout

## Add the data from all other files to the output
for fcurr in "$@"; do
    sed 1d $fcurr
done >> $fout
