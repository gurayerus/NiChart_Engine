import numpy as np
import pandas as pd
import re
from collections import defaultdict
import json
import os
import argparse
import pickle
    
    
######################step 1: clean clincial dataset and reformulate column names ###########################

def clean_clin_data(clin_data_path, var_name):
    '''
    return 
        1) a clean dataframe with naming matching with MRI data 
            - contains column: [ID, MRID, Date, Visit Code, Diagnosis / Cognitive]
            
        2) a flag indicate whether the diagnosis or cognitive variable exist or not(True: Not exist, False: Exist)
      
    inputs:  
        clin_data_path: input data path
        var_name: either diagnosis or cognitive variable
        
        
    ### Note that for clinical data cleaning, we assume the following MRID issues be fixed:
        - BLSA, GSP, HCP-YA, HABS, HCP-Aging, ADNI, UKBB, AIBL 
    '''
    
    flag = False 
    
    df = pd.read_csv(clin_data_path, low_memory = False)
    
    desire_output_col = ['ID','MRID', 'Date', 'Visit_Code', var_name]
    
    for col_name in desire_output_col:
        if col_name not in df.columns:
            df[col_name] = np.nan
            if col_name == var_name:
                flag = True
           
    ### use only desire output columns and drop all nan values for Diagnosis
    df = df[desire_output_col].dropna(subset = [var_name]).reset_index(drop = True)
    return df, flag



######################step 2: Combine MRI data with Clinical Data ###########################
def combined_mri_clin(clin_data_path,
                      mri_data_path, 
                      var_name,
                      study,
                      output_path = None):
    '''
    combined mri and clin data based on MRID, if we don't have MRID, do NOTHING
    input: 
        clin_data_path:  Clinical data path
        mri_data_path:   MRI data path 
        var_name:        Diagnosis or Cogntive Variables
        study:           Study name
        output_path:     output location path
        
    output: 
        A merged csv file with least information, 
        flag (indicate True: variable not exist, False: exist), 
        clincial dataframe (USE FOR VARIABLE EXTRAPOLATION)
    '''
    
    ### a flag indicate whether diagnosis exist or not 
    
    df_mri = pd.read_csv(mri_data_path, low_memory = False)
    df_clin, flag = clean_clin_data(clin_data_path, var_name)
    
    ################################# define three additional column ##############################################
    # diagnosis_IM: diagnosis is missing or not?
    # diagnosis_extrapolate_2.0: extrapolation within 2 years range
    # diagnosis: name matching
    missing_col = '{}_IM'.format(var_name)
    extrapolate_col = '{}_extrapolate'.format(var_name)
    ###############################################################################################################
    
    ### reduce redundant columns
    
    df_total = pd.merge(df_mri, df_clin, on = 'MRID', how = 'left')
    df_total[missing_col] = df_total[var_name].isna()
    df_total[extrapolate_col] = np.nan
    df_total['Study'] = study 
    
    for i in ['ScanDate','VisitCode']:
        if i not in df_total:
            df_total[i] = np.nan 
            
    final_col_use = ['Study','MRID','PID','ScanDate','VisitCode',var_name, missing_col, extrapolate_col ]
    
    if output_path is not None:
        
        df_total[final_col_use].to_csv( os.path.join(output_path, f'{study}_{var_name}_mri_clin_combined.csv'), index = False)
        df_clin.to_csv( os.path.join(output_path, f'{study}_{var_name}_cleaned_clinical.csv'), index = False)

        with open( os.path.join(output_path, f'{study}_{var_name}.pkl'), 'wb') as f:
            pickle.dump(flag, f)
        
        print(f'File has successfully stored at: {output_path}')
    
    return df_total[final_col_use], flag, df_clin



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description = 'Merging MRI and Clinical data!')
    parser.add_argument('-c','--clin_path', type = str, help = 'Clinical input path', default = None)
    parser.add_argument('-m','--mri_path', type = str, help = 'MRI input path', default = None)
    parser.add_argument('-v','--variable_name', type = str, help = 'Variable name', default = None)
    parser.add_argument('-s','--study', type = str, help = 'study name', default = None)
    parser.add_argument('-o','--output_path', type = str, help = 'output_path', default = None)
    
    args = parser.parse_args()
    clin_path = args.clin_path
    mri_path  = args.mri_path
    variable_name  = args.variable_name
    study  = args.study
    output_path = args.output_path 
    
    print('----------Start to Merging MRI and Clinical data-----------------')
    print('Clinical Input Path: ', clin_path)
    print('MRI Input Path: ', mri_path)
    print('Variable Name: ', variable_name)
    print('Study: ', study)
    print('Output Stored at: ', output_path)

    df_combined, flag, df_clin = combined_mri_clin( clin_data_path = clin_path,
                                                    mri_data_path  = mri_path, 
                                                    var_name       = variable_name,
                                                    study          = study,
                                                    output_path    = output_path)

    
    