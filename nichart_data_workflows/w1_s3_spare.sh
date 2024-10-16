#! /bin/bash

# Workflow for preparing initial nichart data:

num_cores=$1
flag='run'
if [ "${num_cores}" == 'dry' ]; then
    flag='dry'
fi
if [ -z $num_cores ]; then
    num_cores='1'
fi

b_dir=$(dirname `pwd`)
s_dir=${b_dir}/src/w_spare

in_roi=${b_dir}/data/output/vTEST/ISTAG_DLMUSE_harmonized.csv
in_demog=${b_dir}/data/output/vTEST/ISTAG_DLMUSE_covars.csv
dset_name='ISTAG'
out_dir=${b_dir}/data/output/vTEST
out_csv=${b_dir}/data/output/vTEST/ISTAG_DLMUSE_SPARE-ALL.csv
res_dir=${b_dir}/resources

cd ${s_dir}

if [ "${flag}" == 'dry' ]; then
    python apply_spare.py --dry_run --in_roi $in_roi --in_demog $in_demog --dset_name $dset_name --out_dir $out_dir --out_csv $out_csv --res_dir $res_dir
else
    python apply_spare.py --in_roi $in_roi --in_demog $in_demog --dset_name $dset_name --out_dir $out_dir --out_csv $out_csv --res_dir $res_dir --num_cores $num_cores
fi


