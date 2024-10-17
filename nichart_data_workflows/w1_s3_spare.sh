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

in_roi=${b_dir}/data/output/ISTAGING-v1.2/ISTAG_train_harmonized.csv
in_demog=${b_dir}/data/output/ISTAGING-v1.2/ISTAG_DLMUSE_covars.csv
out_dir=${b_dir}/data/output/ISTAGING-v1.2
out_dset='ISTAG'
res_dir=${b_dir}/resources

cd ${s_dir}

if [ "${flag}" == 'dry' ]; then
    python apply_spare.py --dry_run --in_roi $in_roi --in_demog $in_demog --out_dir $out_dir --out_dset $out_dset --res_dir $res_dir
else
    python apply_spare.py --in_roi $in_roi --in_demog $in_demog --out_dir $out_dir --out_dset $out_dset --res_dir $res_dir --num_cores $num_cores
fi


