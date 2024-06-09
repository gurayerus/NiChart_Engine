import pandas as pd
import argparse
import json
import sys

def select_spare_sample(in_csv, in_sample, in_vars, out_csv):

    """
    Select data based on list of samples and list of variables
     - in_sample: MRID
     - in_vars: list of variables (MRID,Age)
    """
    
    # Read input files
    df = pd.read_csv(in_csv)
    dfs = pd.read_csv(in_sample)
    
    # Convert columns of dataframe to str (to handle numeric ROI indices)
    df.columns = df.columns.astype(str)

    # Convert in_vars to list
    in_vars = in_vars.split(',')

    # Get key var
    in_key = in_vars[0]

    # Select variables
    df_out = df[in_vars]

    # Select sample
    df_out = dfs.merge(df_out, on = in_key)
    
    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python select_sample.py in_csv.csv in_sample.csv in_vars in_rois.csv out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    in_sample = sys.argv[2]
    in_vars = sys.argv[3]
    out_csv = sys.argv[4]

    # Call the function
    select_spare_sample(in_csv, in_sample, in_vars, out_csv)

    print("SPARE sample selection complete! Output file:", out_csv)

