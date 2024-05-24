import pandas as pd
import argparse
import json
import sys

def filter_data(in_csv, in_filter, out_csv):
    """
    Filters data based on json data
    """
    
    # Read input files
    df = pd.read_csv(in_csv)
    with open(in_filter, "r") as f:
        filter_info = json.load(f)
    
    # Construct filtering condition based on json values
    filter_str = ""
    for filter_dict in filter_info:
        field_name = filter_dict["field_name"]

        ## Filter for min val
        min_val = filter_dict.get("min_val")
        if min_val is not None:
            filter_str += " & " + f"{field_name} >= {min_val}"

        ## Filter for max val
        max_val = filter_dict.get("max_val")
        if max_val is not None:
            filter_str += " & " + f"{field_name} <= {max_val}"

        ## Filter for equal
        eq_val = filter_dict.get("equals")
        if eq_val is not None:
            filter_str += " & " + f"{field_name} == {eq_val}"
            
        ## Filter for isin
        isin_val = filter_dict.get("isin")
        if isin_val is not None:
            filter_str += " & " + f"{field_name}.isin({isin_val})"

        ## Filter for isin
        contains_val = filter_dict.get("contains")
        if contains_val is not None:
            filter_str += " & " + f"{field_name}.str.contains({contains_val})"

    if filter_str.startswith(" & "):
        filter_str = filter_str[3:]

    print("Filtering data using: " + filter_str)

    # Apply filters
    df_out = df.query(filter_str, engine='python')
    
    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 4:
        print("Error: Please provide all required arguments")
        print("Usage: python select_sample.py in_csv.csv in_filter.json out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    in_filter = sys.argv[2]
    out_csv = sys.argv[3]

    # Call the function
    filter_data(in_csv, in_filter, out_csv)

    print("Data filtering complete! Output file:", out_csv)

