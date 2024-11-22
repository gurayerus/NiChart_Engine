#! /bin/bash -x

out_csv=$1
shift

echo "Adding centiles: $1"
cp $1 $out_csv
shift

for arg in "$@"; do
    echo "Adding: $arg"
    sed 1d $arg >> $out_csv
done
