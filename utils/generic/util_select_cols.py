import pandas as pd
import argparse
import json
import sys

def select_cols(in_csv, key_col, cols_keep, out_csv):
    """
    Select columns from data file
    """

    # Read input files
    df = pd.read_csv(in_csv, dtype = {key_col:str})

    # Convert columns of dataframe to str (to handle numeric ROI indices)
    df.columns = df.columns.astype(str)

    # Get variable list 
    cols_keep = cols_keep.split(',')
    
    # Select columns present in df
    cols_keep = [x for x in cols_keep if x in df.columns]

    # Select variables
    df = df[cols_keep]

    # Write out file
    df.to_csv(out_csv, index=False)


if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python select_cols.py in_csv key_col cols_keep out_csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    key_col = sys.argv[2]
    cols_keep = sys.argv[3]
    out_csv = sys.argv[4]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    select_cols(in_csv, key_col, cols_keep, out_csv)

    print("Selection of variables complete! Output file:", out_csv)

