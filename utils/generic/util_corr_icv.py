import pandas as pd
import argparse
import sys

def corr_icv(in_csv, corr_type, icv_var, exclude_vars, out_csv):
    """
    Calculates ICV corrected values
    """
    
    # Set correction factor
    if corr_type == 'percICV':
        corr_val = 100
    if corr_type == 'normICV':
        corr_val = 1430000      ## Average ICV estimated from a large sample
    
    # Read input file
    try:
        df = pd.read_csv(in_csv)
    except:
        print('Error: Could not read input csv file: ' + in_csv)
        return;
    
    # Get var groups
    list_exclude = exclude_vars.split(',') + [icv_var]
    list_target = df.columns[df.columns.isin(list_exclude) == False]
    df_p1 = df[list_exclude]
    df_p2 = df[list_target]
    val_icv = df[icv_var]
    
    # Correct ICV
    df_p2 = df_p2.div(val_icv, axis=0)*corr_val
    
    # Combine vars
    df_out = pd.concat([df_p1, df_p2], axis = 1)
    
    # Write out file
    df_out.to_csv(out_csv, index=False)
    print("ICV correction complete! Output file:", out_csv)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 6:
        print("Error: Please provide all required arguments")
        print("Usage: python corr_icv.py in_csv.csv corr_type icv_var exclude_vars out_csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    corr_type = sys.argv[2]
    icv_var = sys.argv[3]
    exclude_vars = sys.argv[4]
    out_csv = sys.argv[5]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    # Call the function
    corr_icv(in_csv, corr_type, icv_var, exclude_vars, out_csv)


