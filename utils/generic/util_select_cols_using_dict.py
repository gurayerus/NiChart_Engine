import pandas as pd
import argparse
import json
import sys

def select_cols_using_dict(in_csv, key_col, cols_keep, dict_csv, dict_col, out_csv):
    """
    Select columns from data file using a dictionary 
    Combines a list of selected columns with column names read from a dictionary (e.g. for ROI names)
    """

    # Read input files
    df = pd.read_csv(in_csv, dtype = {key_col:str})
    dfd = pd.read_csv(dict_csv)

    # Convert columns of dataframe to str (to handle numeric ROI indices)
    df.columns = df.columns.astype(str)

    # Get variable lists
    cols_keep = cols_keep.split(',')    
    list_cols = dfd[dict_col].astype(str).tolist()

    # Select columns present in df
    list_cols = [x for x in list_cols if x in df.columns]

    # Select columns not selected in columns to keep
    list_cols = [x for x in list_cols if x not in cols_keep]
    
    # Create list of sele columns
    list_cols = cols_keep + list_cols

    # Select variables
    df = df[list_cols]

    # Write out file
    df.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 7:
        print("Error: Please provide all required arguments")
        print("Usage: python select_cols_using_dict.py in_csv key_col cols_keep dict_csv dict_col out_csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    key_col = sys.argv[2]
    cols_keep = sys.argv[3]
    dict_csv = sys.argv[4]
    dict_col = sys.argv[5]
    out_csv = sys.argv[6]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    select_cols_using_dict(in_csv, key_col, cols_keep, dict_csv, dict_col, out_csv)

    print("Selection of variables complete! Output file:", out_csv)

