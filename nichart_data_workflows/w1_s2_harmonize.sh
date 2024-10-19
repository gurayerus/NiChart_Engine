#! /bin/bash +x

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
s_dir=${b_dir}/src/w_harmonize

in_roi=${b_dir}/data/output/vTEST/data/ISTAG_DLMUSE_raw.csv
in_demog=${b_dir}/data/output/vTEST/covars/ISTAG_DLMUSE_covars.csv
dset_name='ISTAG'
out_dir=${b_dir}/data/output/vTEST
out_mdl=${b_dir}/data/output/vTEST/models/ISTAG_DLMUSE_raw_mdlCOMBAT.pkl.gz
out_roi=${b_dir}/data/output/vTEST/data/ISTAG_DLMUSE_raw_harmonized.csv
res_dir=${b_dir}/resources

cd ${s_dir}

if [ "${flag}" == 'dry' ]; then
    python harmonize_data.py --dry_run --in_roi $in_roi --in_demog $in_demog --dset_name $dset_name --out_dir $out_dir --out_mdl $out_mdl --out_roi $out_roi --res_dir $res_dir
else
    python harmonize_data.py --in_roi $in_roi --in_demog $in_demog --dset_name $dset_name --out_dir $out_dir --out_mdl $out_mdl --out_roi $out_roi --res_dir $res_dir --num_cores $num_cores
fi


