#! /bin/bash

# Workflow for preparing initial nichart data:

flag=$1

b_dir=$(dirname `pwd`)
s_dir=${b_dir}/src/w_harmonize

in_roi=${b_dir}/data/output/ISTAGING-v1.2/ISTAG_DLMUSE_raw.csv
in_demog=${b_dir}/data/output/ISTAGING-v1.2/ISTAG_DLMUSE_covars.csv
out_dir=${b_dir}/data/output/ISTAGING-v1.2
out_dset='ISTAG'
res_dir=${b_dir}/resources

cd ${s_dir}

if [ "${flag}" == '--dry' ]; then
    python harmonize_data.py --dry_run --in_roi $in_roi --in_demog $in_demog --out_dir $out_dir --out_dset $out_dset --res_dir $res_dir
else
    python harmonize_data.py --in_roi $in_roi --in_demog $in_demog --out_dir $out_dir --out_dset $out_dset --res_dir $res_dir
fi


