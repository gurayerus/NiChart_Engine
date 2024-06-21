import pandas as pd
import argparse
import sys

def filter_var(in_csv, var_name, min_val, max_val, out_csv):
    """
    Filter df based on range of values for the variable
    """
    
    # Read input file
    df = pd.read_csv(in_csv)
    
    # Filter df
    df = df[df[var_name]>=min_val]
    df = df[df[var_name]<=max_val]
    
    # Write out file
    df.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 6:
        print("Error: Please provide all required arguments")
        print("Usage: python filter_var.py in_csv.csv var_name min_val max_val out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    var_name = sys.argv[2]
    min_val = float(sys.argv[3])
    max_val = float(sys.argv[4])
    out_csv = sys.argv[5]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    filter_var(in_csv, var_name, min_val, max_val, out_csv)

    print("ROI QC complete! Output file:", out_csv)
