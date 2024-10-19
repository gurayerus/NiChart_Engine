import argparse
import json
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--in_dir", help="Provide input data folder name", required=True
    )
    parser.add_argument(
        "--in_demog", help="Provide input demog file name", required=True
    )
    parser.add_argument(
        "--dset_name", help="Provide output dataset name", required=True
    )
    parser.add_argument(
        "--out_dir", help="Provide output folder name", required=True
    )
    parser.add_argument(
        "--res_dir", help="Provide folder name with shared resources", required=True
    )
    parser.add_argument(
        "--num_cores", help="Provide number of cores", required=False
    )
    parser.add_argument(
        "--dry_run", help="Set flag for dry run", action="store_true"
    )

    options = parser.parse_args()

    # Create out dir
    if not os.path.exists(options.out_dir):
        os.makedirs(options.out_dir)

    # Run workflow
    print(f"Running: snakemake")

    cmd = "snakemake"
    if options.dry_run:
        cmd = cmd + " -np"
    cmd = cmd + " --config in_dir=" + options.in_dir
    cmd = cmd + " in_demog=" + options.in_demog
    cmd = cmd + " dset_name=" + options.dset_name
    cmd = cmd + " out_dir=" + options.out_dir
    cmd = cmd + " res_dir=" + options.res_dir
    if not options.dry_run:
        cmd = cmd + " --cores 1"

    print("Running cmd: " + cmd)

    os.system(cmd)
