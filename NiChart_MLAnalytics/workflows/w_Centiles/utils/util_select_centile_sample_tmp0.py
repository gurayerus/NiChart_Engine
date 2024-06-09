import pandas as pd
import argparse
import json
import sys

def select_sample(in_csv, in_sample, in_vars, out_csv):

    """
    Select data based on list of samples and list of variables
     - in_sample: MRIDs of samples
     - in_vars: list of variables
     - in_rois: list of additional ROI variables (with columns Index,Name)
                the column Name is used to select additional ROI variables
     - in_var_names: list of var names to rename additional variables
    """
    
    # Read input files
    df = pd.read_csv(in_csv)
    dfs = pd.read_csv(in_sample)
    
    # Convert columns of dataframe to str (to handle numeric ROI indices)
    df.columns = df.columns.astype(str)

    # Check if rois list provided
    in_vars = in_vars.split(',')
    if in_rois == 'None':
        sel_vars = in_vars
    
    else:
        dfr = pd.read_csv(in_rois)

        # Get variable lists (input var list + rois)
        roi_vars = dfr.Name.astype(str).tolist()
    
        # Remove duplicate vars (in case a variable is both in roi list and input var list)
        in_vars = [x for x in in_vars if x not in roi_vars]

        # Make a list of selected variables
        sel_vars = in_vars + roi_vars 
        
    # Get key var
    in_key = sel_vars[0]
    
    # Select variables
    df_out = df[sel_vars]

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
    select_sample(in_csv, in_sample, in_vars, out_csv)

    print("Sample selection complete! Output file:", out_csv)

