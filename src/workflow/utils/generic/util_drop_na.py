import pandas as pd
import argparse
import json
import sys

def drop_na(in_csv, out_csv):
    """
    Drop nas from data
    """
    
    # Read input file
    df = pd.read_csv(in_csv, dtype = {'MRID':str})

    # Drop nas
    df_out = df.dropna()

    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 3:
        print("Error: Please provide all required arguments")
        print("Usage: python drop_na.py in_csv out_csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    out_csv = sys.argv[2]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    drop_na(in_csv, out_csv)

    print("Drop na complete! Output file:", out_csv)

