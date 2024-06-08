import pandas as pd
import sys
import os

def subsample_data(in_csv, num_sample, out_vars, out_csv):
    """
    Select a subsample of the data.
    """

    ## Read data
    df = pd.read_csv(in_csv)
    
    ## Select sample
    df_out = df.sample(num_sample)
    
    ## Get out variables(s)
    out_vars = out_vars.split(',')
    df_out = df_out[out_vars]

    ## Write output
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python subsample_data.py in_csv.csv num_sample out_vars out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    num_sample = int(sys.argv[2])
    out_vars = sys.argv[3]
    out_csv = sys.argv[4]
    
    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    subsample_data(in_csv, num_sample, out_vars, out_csv)

    print("Sample selection complete! Output file:", out_csv)
