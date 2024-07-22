import pandas as pd
import argparse
import json
import sys

def rename_column(in_csv, num_col, name_col, out_csv):

    """
    Rename column of data file
    """
    
    # Read input file
    df = pd.read_csv(in_csv, dtype = {'MRID':str})

    # Convert num col to int
    num_col=int(num_col)

    # Rename column
    df_out = df.rename(columns = {df.columns[num_col]:name_col})

    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python rename_column.py in_csv num_col name_col out_csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    num_col = sys.argv[2]
    name_col = sys.argv[3]
    out_csv = sys.argv[4]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    rename_column(in_csv, num_col, name_col, out_csv)

    print("Renaming of column complete! Output file:", out_csv)

