import pandas as pd
import sys
import os

def filter_to_subsampled(in_csv, ref_csv, key_col, out_csv):
    ## Read data
    df = pd.read_csv(in_csv)
    df_ref = pd.read_csv(ref_csv)

    ## Select sample
    df_ref = df_ref[[key_col]]
    df_out = df_ref.merge(df, on=key_col, how='inner')

    ## Write output
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python filter_to_subsampled.py in_csv.csv ref_csv.csv key_var out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    ref_csv = sys.argv[2]
    key_var = sys.argv[3]
    out_csv = sys.argv[4]
    
    # Call the function
    if ref_csv != out_csv:
        filter_to_subsampled(in_csv, ref_csv, key_var, out_csv)
        print("Sample selection complete! Output file:", out_csv)
    else:
        print("Skip sample selection, ref file same as out file!")
