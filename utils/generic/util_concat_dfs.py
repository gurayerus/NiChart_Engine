import pandas as pd
import sys

def concat_dfs(out_csv, list_in_csv):
    """
    Concat multiple input data files
    Output data includes only common variables to all files
    """
    list_df = []
    col_common = []
    for i, in_csv in enumerate(list_in_csv):
        try:
            # Read csv files
            df_tmp = pd.read_csv(in_csv, dtype = {'MRID':str})
            list_df.append(df_tmp)

            # Detect common columns
            col_tmp = df_tmp.columns
            if col_common == []:
                col_common = df_tmp.columns.tolist()
            col_common = [x for x in df_tmp.columns if x in col_common]
             
        except:
            print('Warning: Could not read csv file, skipping: ' + in_csv)

    try:
        # Concat data
        df_out = pd.concat(list_df)

        # Select common columns
        df_out = df_out[col_common]

        # Write out file
        df_out.to_csv(out_csv, index=False)
        
        print("Concatation complete! Output file:", out_csv)
        
    except:
        print('Error: Concatation failed')


if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) < 3:
        print("Error: Please provide all required arguments")
        print("Usage: python concat_dfs.py out_csv.csv in_csv1.csv in_csv2.csv ...")
        sys.exit(1)

    out_csv = sys.argv[1]
    list_in_csv = sys.argv[2:]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    concat_dfs(out_csv, list_in_csv)
