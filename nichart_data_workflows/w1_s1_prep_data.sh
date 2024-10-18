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
s_dir=${b_dir}/src/w_prep_data

in_dir=${b_dir}/data/input/ISTAGING-v1.2
dset_name='ISTAG'
out_dir=${b_dir}/data/output/vTEST
res_dir=${b_dir}/resources

cd ${s_dir}

if [ "${flag}" == 'dry' ]; then
    python prep_data.py --dry_run --in_dir $in_dir --out_dir $out_dir --dset_name $dset_name --res_dir $res_dir --num_cores $num_cores
else
    python prep_data.py --in_dir $in_dir --out_dir $out_dir --dset_name $dset_name --res_dir $res_dir --num_cores $num_cores
fi
