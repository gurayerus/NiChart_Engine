import numpy as np
import pandas as pd
import re
from collections import defaultdict
import json
import os
import argparse
import pickle


######################step 3: Diagnosis Column extrapolation ###########################
def find_closest_value_visit_code(row, df2, diagnosis): 
    
    '''
    when Date is not avaiable, chose visit code instead
    input:
        row: a row for each MRI data
        df2: a cleaned clinical data contains diagnosis, PID, VisitCode 
        diagnosis: diagnosis 
    
    output:
        a panda series with two values [diagnosis, how much close (0 means the value is already there, 1 means the data is extrapolate with the nearest 1 day)
    '''
     
    if not pd.isna(row[diagnosis]):
        return pd.Series([row[diagnosis],0])
    
    id = row['PID']
    vs = row['VisCode']
    
    filtered_df2 = df2[(df2['ID'] == id)] ## Same Subject 
   
    
    filtered_df2 = filtered_df2[[diagnosis,'Visit_Code']].dropna()
    
    if filtered_df2.empty:
        return None
    
    else:
        filtered_df2['date-diff'] = filtered_df2['Visit_Code'].apply(lambda x: abs(int(x) - int(vs)))
        min_diff = filtered_df2['date-diff'].min()
        closest_row = filtered_df2[filtered_df2['date-diff'] == min_diff]
        result = closest_row[diagnosis].iloc[0]
        return pd.Series([result, min_diff])
        
    
def find_closest_value_date(row, df2, diagnosis):    
    
    '''
    use date as the main part
    input:
        row: a row for each MRI data
        df2: a cleaned clinical data contains diagnosis, PID, Date
        diagnosis: diagnosis 
    
    output:
        a panda series with two values [diagnosis, how much close (0 means the value is already there, 1 means the data is extrapolate with the nearest 1 day)
    '''
    
    if not pd.isna(row[diagnosis]):
        return pd.Series([row[diagnosis],0])
    
    id = row['PID']
    date = row['ScanDate']
    
    if pd.isna(date):
        return pd.Series([np.nan, np.nan])
    
    filtered_df2 = df2[df2['ID'] == id]
    filtered_df2 = filtered_df2[[diagnosis,'Date']].dropna()
    
    if filtered_df2.empty:
        return pd.Series([np.nan, np.nan])
    
    else:
        filtered_df2['date-diff'] = filtered_df2['Date'].apply(lambda x: abs(x - date))
        min_diff = filtered_df2['date-diff'].min()
        closest_row = filtered_df2[filtered_df2['date-diff'] == min_diff ]
        result = closest_row[diagnosis].iloc[0]
        return pd.Series([result, min_diff.days])
        
def find_closest_value_visit_code(row, df2, diagnosis): 
    
    '''
    when Date is not avaiable, chose visit code instead
    input:
        row: a row for each MRI data
        df2: a cleaned clinical data contains diagnosis, PID, VisitCode 
        diagnosis: diagnosis 
    
    output:
        a panda series with two values [diagnosis, how much close (0 means the value is already there, 1 means the data is extrapolate with the nearest 1 day)
    '''
     
    if not pd.isna(row[diagnosis]):
        return pd.Series([row[diagnosis],0])
    
    id = row['PID']
    vs = row['VisitCode']
    
    filtered_df2 = df2[(df2['ID'] == id)] ## Same Subject 
   
    
    filtered_df2 = filtered_df2[[diagnosis,'Visit_Code']].dropna()
    
    if filtered_df2.empty:
        return None
    
    else:
        filtered_df2['date-diff'] = filtered_df2['Visit_Code'].apply(lambda x: abs(int(x) - int(vs)))
        min_diff = filtered_df2['date-diff'].min()
        closest_row = filtered_df2[filtered_df2['date-diff'] == min_diff]
        result = closest_row[diagnosis].iloc[0]
        return pd.Series([result, min_diff])
        
    
def find_closest_value_date(row, df2, diagnosis):    
    
    '''
    use date as the main part
    input:
        row: a row for each MRI data
        df2: a cleaned clinical data contains diagnosis, PID, Date
        diagnosis: diagnosis 
    
    output:
        a panda series with two values [diagnosis, how much close (0 means the value is already there, 1 means the data is extrapolate with the nearest 1 day)
    '''
    
    if not pd.isna(row[diagnosis]):
        return pd.Series([row[diagnosis],0])
    
    id = row['PID']
    date = row['ScanDate']
    
    if pd.isna(date):
        return pd.Series([np.nan, np.nan])
    
    filtered_df2 = df2[df2['ID'] == id]
    filtered_df2 = filtered_df2[[diagnosis,'Date']].dropna()
    
    if filtered_df2.empty:
        return pd.Series([np.nan, np.nan])
    
    else:
        filtered_df2['date-diff'] = filtered_df2['Date'].apply(lambda x: abs(x - date))
        min_diff = filtered_df2['date-diff'].min()
        closest_row = filtered_df2[filtered_df2['date-diff'] == min_diff ]
        result = closest_row[diagnosis].iloc[0]
        return pd.Series([result, min_diff.days])
        
    
def extrapolation(combined_df_,
                  clin_df, 
                  Diagnosis,  
                  flag = False):
    
    '''
    Perform extrapolation on the dataset, return a new dataframe with extrapolated values
    
    Input: 
        combined_df:     combined dataframe from step 1 (the combination of clinical and mri data)
        clin_df:         a cleaned version of clinical data
        Diagnosis:       Diagnosis
        flag:            True if clin_input_dic doesn't contain Diagnosis 
    '''
    
    combined_df = combined_df_
    diagnosis_missing_col = '{}_IM'.format(Diagnosis)
    diagnosis_extrapolate_col = '{}_extrapolate'.format(Diagnosis)
    
    if Diagnosis not in combined_df.columns:
        combined_df[Diagnosis] = np.nan 
        
    if diagnosis_missing_col not in combined_df.columns:
        combined_df[diagnosis_missing_col] = True 
    
    if diagnosis_extrapolate_col not in combined_df.columns:
        combined_df[diagnosis_extrapolate_col] = np.nan 
        
        
    final_col = ['Study','MRID','PID',Diagnosis, diagnosis_missing_col, diagnosis_extrapolate_col, 'Delta']
    
    #### directly return combined df if diagnosis doesn't exist
    if flag: 
        combined_df['Delta'] = np.nan
        return combined_df[final_col]
    
    #####
    study = combined_df['Study'].unique()[0]
     
    df_clin = clin_df 
    df_total = combined_df
    df_total['Delta'] = np.nan
        
    if 'Date' in df_clin.columns and df_clin['Date'].isna().sum() != len(df_clin): ### if Date exist 
        df_clin['Date'] = pd.to_datetime(df_clin['Date'])
        df_total['ScanDate'] = pd.to_datetime(df_total['ScanDate'])
        
        df_total[[diagnosis_extrapolate_col, 'Delta']] = df_total.apply(lambda row: find_closest_value_date(row, df_clin, Diagnosis), axis = 1)
        
    elif df_clin['Visit_Code'].isna().sum() != len(df_clin): ### if Visit_Code exist
        df_clin = df_clin[~df_clin['Visit_Code'].isin(['dNA','NA'])]
        df_clin['Visit_Code']=df_clin['Visit_Code'].apply(lambda x: int(x[1:]))
        df_total['VisitCode']= df_total['VisitCode'].apply(lambda x: int(x[1:]))  
    
        df_total[[diagnosis_extrapolate_col,'Delta']] = df_total.apply(lambda row: find_closest_value_visit_code(row, df_clin, Diagnosis), axis = 1)
            
    return df_total[final_col]



######################step 4: column name conversion + value grouping ###########################
def col_name_conversion(df, diagnosis, diagnosis_value_mapping, study, var_type = 'DX', output_path = None):
    '''
    maping: diganosis to user-defined name
    format: 
        {}_{Diagnosis}_NC
        {}_{Diagnosis_IM}_NC
        {}_{Diagnosis_extrapolate}_NC
        {}_{Diagnosis}_delta_NC
    '''
    
    diagnosis_conversion_dic = {
        'Diagnosis': 'AD'
    }
    
    ### based on Liz Code for Diagnosis Mapping (other than AD-Diagnosis)
    clin_map = {0 : 'Negative/absent',
                1 : 'Positive/present',
                2 : 'Remote/inactive',
                5 : 'Pre-Diabetes',
                8 : 'Unknown'
    }
    
    prefix = var_type
    
    if diagnosis not in diagnosis_conversion_dic.keys():
        conversion_name = diagnosis
    else:
        conversion_name = diagnosis_conversion_dic[diagnosis]
    
    #-----------------------------------------------------------
    study = df.loc[0, 'Study']
    df['{}_{}_is_imputation_NC'.format(prefix, conversion_name)] = False
    
    if study and study == 'UKBB':
        df['{}_{}_is_imputation_NC'.format(prefix, conversion_name)] = df[diagnosis].isna()
        df['{}_extrapolate'.format(diagnosis)] = df['{}_extrapolate'.format(diagnosis)].fillna('CN')
    
    #------------------------------------------------------------
    
    diganosis_col_name = '{}_{}_original_NC'.format(prefix, conversion_name)
    diganosis_missing_col_name = '{}_{}_IM_NC'.format(prefix, conversion_name)
    diagnosis_extrapolate_col_name = '{}_{}_Multi_Class_NC'.format(prefix, conversion_name)
    diagnosis_delta_col_name = '{}_{}_delta_NC'.format(prefix, conversion_name)
    
    df = df.rename(columns = {diagnosis:diganosis_col_name ,
                         '{}_IM'.format(diagnosis): diganosis_missing_col_name,
                         '{}_extrapolate'.format(diagnosis):diagnosis_extrapolate_col_name,
                         'Delta' : diagnosis_delta_col_name})
    
    if diagnosis == 'Diagnosis':
        df['{}_{}_NC'.format(prefix, conversion_name)] = df[diagnosis_extrapolate_col_name].replace(diagnosis_value_mapping)
    elif prefix == 'DX':
        df['{}_{}_NC'.format(prefix, conversion_name)] = df[diagnosis_extrapolate_col_name].replace(clin_map)
    elif prefix == 'CO':
        df['{}_{}_NC'.format(prefix, conversion_name)] = df[diagnosis_extrapolate_col_name]
    else:
        ### current do nothing, will add more functionalities later...
        pass
    
    if output_path is not None:
        df.to_csv( os.path.join(output_path, f'{study}_{var_type}_{conversion_name}.csv'))
        print(f'File has successfully stored at: {output_path}')

    return df



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description = 'Merging MRI and Clinical data!')
    parser.add_argument('-i','--input_path', type = str, help = 'Clinical MRI combined Data input path', default = None)
    parser.add_argument('-v','--variable_name', type = str, help = 'Variable name', default = None)
    parser.add_argument('-s','--study', type = str, help = 'study name', default = None)
    parser.add_argument('-o','--output_path', type = str, help = 'output_path', default = None)
    parser.add_argument('-vt','--var_type', type = str, help = 'variable type', default = 'DX' , choices=['DX', 'CO'])
    parser.add_argument('-mp' ,'--map_dic_path', type = str, help = 'mapping dictionary json', default = None)

    
    args = parser.parse_args()
    input_path = args.input_path
    variable_name  = args.variable_name
    study     = args.study
    output_path = args.output_path 
    var_type  = args.var_type
    map_dic_path = args.map_dic_path
    
    print('----------Start to do extrapolation-----------------')
    print('Input Path: ', input_path)
    print('Variable Name: ', variable_name)
    print('Study: ', study)
    print('Var type: ', var_type)
    print('Mapping dictionary Path: ', map_dic_path)
    print('Output Stored at: ', output_path)

    
    if os.path.exists( os.path.join(input_path, f'{study}_{variable_name}_mri_clin_combined.csv') ):
        
        df_combined = pd.read_csv( os.path.join(input_path, f'{study}_{variable_name}_mri_clin_combined.csv') )
        with open( os.path.join(input_path, f'{study}_{variable_name}.pkl'), 'rb') as f:
            flag = pickle.load(f)
            
        df_clin = pd.read_csv( os.path.join(input_path, f'{study}_{variable_name}_cleaned_clinical.csv') )
        
    else:
        raise Exception("The files are not exist in the path, please use a valid path.")
    
    with open( os.path.join(map_dic_path, 'diagnosis_value_mapping.json'), 'r') as json_file:
        diagnosis_value_mapping = json.load(json_file)

    ## step 3: exptrapolation
    data = extrapolation(combined_df_ = df_combined,
                         clin_df = df_clin, 
                         Diagnosis = variable_name,  
                         flag = flag)
    
    ##  step 4: conversion the name 
    result = col_name_conversion(df = data, 
                                 diagnosis = variable_name, 
                                 diagnosis_value_mapping = diagnosis_value_mapping , 
                                 var_type = var_type, 
                                 study = study,
                                 output_path = output_path)
    
    
    
    
    