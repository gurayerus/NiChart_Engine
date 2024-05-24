import pandas as pd
import argparse
from SurrealGAN.Surreal_GAN_representation_learning import repetitive_representation_learning
import os
import sys

if __name__ == '__main__':

    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python util_surrealgan_train.py in_data.csv in_covar.csv in_start_fold out_dir")
        sys.exit(1)

    #####################
    ## Hard-coded args (FIXME: would be better to read those from a config file!)
    npattern = 5
    
    ##final_saving_epoch = 63000
    ##saving_freq=2500
    ##fold_number = 50
    ##early_stop_thresh = 0.005

    final_saving_epoch = 63     ## FIXME this is temp for a quick run
    saving_freq = 25
    fold_number = 5
    early_stop_thresh = 0.05
    
    lr = 0.0008
    batchsize=300
    verbose=True
    lipschitz_k=0.5
    lam=0.8
    gamma=0.1

    #####################
    ## User args
    in_data = sys.argv[1]
    in_covar = sys.argv[2]
    in_start_fold = int(sys.argv[3])
    out_mdl = sys.argv[4]

    ## Calculate additional args
    stop_fold = in_start_fold + 1
    
    out_dir = os.path.dirname(out_mdl)
    
    ## Read data
    df_data = pd.read_csv(in_data)
    df_covar = pd.read_csv(in_covar)

    #####################
    # Call the function
    repetitive_representation_learning(df_data, 
                                       npattern, 
                                       fold_number, 
                                       1,
                                       final_saving_epoch, 
                                       out_dir, 
                                       lr = lr, 
                                       batchsize = batchsize, 
                                       verbose = verbose,
                                       lipschitz_k = lipschitz_k, 
                                       covariate = df_covar,
                                       lam = lam, 
                                       gamma = gamma, 
                                       saving_freq = saving_freq, 
                                       start_repetition = in_start_fold, 
                                       stop_repetition = stop_fold, 
                                       early_stop_thresh = early_stop_thresh)

    print("Surreal-gan complete! Output dir:", out_dir)



