import argparse
import json
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--in_dir", help="Provide input folder name", required=True
    )
    parser.add_argument(
        "--out_dir", help="Provide output folder name", required=True
    )
    parser.add_argument(
        "--out_dset", help="Provide output dataset name", required=True
    )
    parser.add_argument(
        "--res_dir", help="Provide folder name with shared resources", required=True
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
    cmd = cmd + " out_dir=" + options.out_dir
    cmd = cmd + " out_dset=" + options.out_dset
    cmd = cmd + " res_dir=" + options.res_dir
    cmd = cmd + " --cores 1"

    print("Running cmd: " + cmd)

    os.system(cmd)
