import pandas as pd
import numpy as np
import sys

def eval_spare(in1_csv, in2_csv, target_var, out_csv):
    """
    Merge two input data files
    Output data includes an inner merge
    """
    
    key_var = 'MRID'
    
    # Read csv files
    df1 = pd.read_csv(in1_csv)
    df2 = pd.read_csv(in2_csv)
    
    df1 = df1[[key_var, target_var]]
    df2 = df2[[key_var, target_var]]

    # Merge DataFrames
    df_tmp = df1.merge(df2, on = key_var, suffixes = ['_init', '_pred'])

    # Calculate score
    num_label = df1[target_var].unique().shape[0]
    num_sample = df1.shape[0]
    v1 = df_tmp[target_var + '_init']
    v2 = df_tmp[target_var + '_pred']
    
    if num_label == 2:      ## Classification
        out_score = float((v1==v2).sum()) / num_sample
        out_label = 'Accuracy'

    else:      ## Regression
        out_score = np.corrcoef(v1==v2)[0,1]
        out_label = 'CorrCoef'

    df_out = pd.DataFrame(columns = [out_label], data = out_score)

    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python eval_spare.py in1_csv.csv in2_csv.csv target_var out_csv.csv")
        sys.exit(1)

    in1_csv = sys.argv[1]
    in2_csv = sys.argv[2]
    target_var = sys.argv[3]
    out_csv = sys.argv[4]

    # Call the function
    eval_spare(in1_csv, in2_csv, target_var, out_csv)

    print("Evaluation complete! Output file:", out_csv)
