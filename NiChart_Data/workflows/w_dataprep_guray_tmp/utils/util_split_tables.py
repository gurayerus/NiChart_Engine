import pandas as pd
import sys
import os

def split_tables(in_csv, dict_csv, out_pref, tables):
    ## Read data
    df = pd.read_csv(in_csv)
    df_dict = pd.read_csv(dict_csv)

    list_tables = tables.split(',')
    
    for tmp_table in list_tables:
        ## Select variables
        sel_vars = df_dict[df_dict.VAR_CAT=='KEYS'].VAR_NAME.tolist() + df_dict[df_dict.VAR_CAT==tmp_table].VAR_NAME.to_list()
        df_out = df[sel_vars]
        df_out.to_csv(out_pref + '_' + tmp_table + '.csv', index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python split_tables.py in_csv.csv dict.csv out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    dict_csv = sys.argv[2]
    out_pref = sys.argv[3]
    tables = sys.argv[4]
    
    # Call the function
    split_tables(in_csv, dict_csv, out_pref, tables)
    print("Sample selection complete! Output file:", out_pref, ' ... ' )
