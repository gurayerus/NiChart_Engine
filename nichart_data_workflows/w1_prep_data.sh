#! /bin/bash

# Workflow for preparing initial nichart data:

flag=$1

b_dir=$(dirname `pwd`)
s_dir=${b_dir}/src/w_prep_data

in_dir=${b_dir}/data/input/ISTAGING-v1.2
out_dir=${b_dir}/data/output/ISTAGING-v1.2
out_dset='ISTAG'
res_dir=${b_dir}/resources

cd ${s_dir}

if [ "${flag}" == '--dry' ]; then
    python prep_data.py --dry_run --in_dir $in_dir --out_dir $out_dir --out_dset $out_dset --res_dir $res_dir
else
    python prep_data.py --in_dir $in_dir --out_dir $out_dir --out_dset $out_dset --res_dir $res_dir
fi


