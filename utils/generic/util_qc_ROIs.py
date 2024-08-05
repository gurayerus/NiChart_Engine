import pandas as pd
import argparse
import sys

def qc_ROIs(in_csv, out_csv):
    """
    QC ROIs based on fixed rules
    """
    
    # Read input file
    df = pd.read_csv(in_csv)
    
    # Excluse QC fail cases
    df['rateICV'] = df.DLICV / df.MUSE_702
    df = df[df.rateICV > 0.75]
    df = df[df.rateICV < 1.25]
    df = df[df.DLICV > 800000]    
    df = df[df.DLICV > 800000]
    df = df[df.MUSE_702 > 800000]
    df = df[df.MUSE_702 > 800000]
    
    # Write out file
    df.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 3:
        print("Error: Please provide all required arguments")
        print("Usage: python qc_ROIs.py in_csv.csv out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    out_csv = sys.argv[2]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    # Call the function
    qc_ROIs(in_csv, out_csv)

    print("ROI QC complete! Output file:", out_csv)

