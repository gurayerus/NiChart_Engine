import pandas as pd
import argparse
import json
import sys

def select_vars_from_list(in_csv, vars_list, out_csv):
    """
    Select variables from data file
    """

    # Read input files
    df = pd.read_csv(in_csv, dtype = {'MRID':str})

    # Get variable lists (input var list + rois)
    vars_list = vars_list.split(',')
    vars_list = [x for x in df.columns]

    # Select variables
    df = df[sel_vars]

    # Write out file
    df.to_csv(out_csv, index=False)


if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 4:
        print("Error: Please provide all required arguments")
        print("Usage: python select_vars.py in_csv vars_list out_csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    vars_list = sys.argv[2]
    out_csv = sys.argv[3]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    select_vars_from_list(in_csv, vars_list, out_csv)

    print("Selection of variables complete! Output file:", out_csv)

