import pandas as pd
import argparse
import json
import sys

def rename_rois(in_csv, in_rois, out_csv):
    """
    Rename roi names in input csv
    """
    
    # Read input files
    df = pd.read_csv(in_csv)
    dfs = pd.read_csv(in_rois)
    
    # Roi dictionary
    rdict = dict(zip(dfs.Code, dfs.Name))
    
    # Rename column
    df['VarName'] = df.VarName.replace(rdict)
    
    # Write out file
    df.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 4:
        print("Error: Please provide all required arguments")
        print("Usage: rename_rois.py in_csv.csv in_rois.csv out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    in_rois = sys.argv[2]
    out_csv = sys.argv[3]

    # Call the function
    rename_rois(in_csv, in_rois, out_csv)

    print("ROI renaming complete! Output file:", out_csv)

