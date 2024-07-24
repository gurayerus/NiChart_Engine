#!/bin/bash

#SBATCH --mem=32000
#SBATCH --output=slurm_logs/snakemake-%j.out

source activate /cbica/home/erusg/.conda/envs/snakemake-tutorial
# source activate /cbica/home/erusg/.conda/envs/spare

# snakemake --cores=1 --executor slurm --default-resources slurm_account=davatzic --jobs 1 
snakemake --cores=1 --executor slurm --default-resources slurm_account=davatzic --jobs 10 

# apptainer run ${SNAKEMAKE_DIR}/snakemake.sif --cores 1

conda deactivate
