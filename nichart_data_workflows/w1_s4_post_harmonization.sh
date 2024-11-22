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
s_dir=${b_dir}/src/w_post_harmonization

in_dir=${b_dir}/data/input/ISTAGING-v1.2
in_demog=${b_dir}/data/output/ISTAGING-v1.2/covars/ISTAG_DLMUSE_covars.csv
dset_name='ISTAG'
out_dir=${b_dir}/data/output/ISTAGING-v1.2
res_dir=${b_dir}/resources

cd ${s_dir}

if [ "${flag}" == 'dry' ]; then
    python post_harmonization.py --dry_run --in_dir $in_dir --in_demog $in_demog --out_dir $out_dir --dset_name $dset_name --res_dir $res_dir --num_cores $num_cores
else
    python post_harmonization.py --in_dir $in_dir --in_demog $in_demog --out_dir $out_dir --dset_name $dset_name --res_dir $res_dir --num_cores $num_cores
fi