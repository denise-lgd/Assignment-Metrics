import pandas as pd
import csv
from math import log

#load dataframes from results folder
df_ck_506 = pd.read_csv('results/ckjm/ckjm_5.0.6.csv')
df_ck_513 = pd.read_csv('results/ckjm/ckjm_5.1.3.csv')
df_ck_521 = pd.read_csv('results/ckjm/ckjm_5.2.1.csv')
df_ck_534 = pd.read_csv('results/ckjm/ckjm_5.3.4.csv')
df_ck_545 = pd.read_csv('results/ckjm/ckjm_5.4.5.csv')
df_ck_55133 = pd.read_csv('results/ckjm/ckjm_5.5.13.3.csv')

#make list of dataframes to loop over
dataframes = [df_ck_506,df_ck_513,df_ck_521,df_ck_534,df_ck_545,df_ck_55133]

def calculate_FWBR(dataframes):
    '''Calculates the FWBR value as defined in the assignment for each dataframe and adds
    these values as a new column in the dataframe.'''
    for dataframe in dataframes:
        FWBR_values = []
        for index, row in dataframe.iterrows():
            FWBR = -1 * (8.753 * log(row['CBO']+1,10)) + 2.505 * (log(row['DIT'] +1,10)) - 1.922 * (log(row['WMC'] +1,10)) + 0.89 * (log(row['RFC']+1,10)) -0.399 * (log(row['LCOM']+1,10)) -1.08 * (log(row['NOC']+1,10))
            FWBR_values.append(FWBR)
        dataframe["FWBR"]=FWBR_values

def calculate_FWBR_subs(dataframes):
    '''Checks the length of the dataframe (amount of rows = amount of classes) and calculates
    the sub-metric FWBR defined on this and adds this as a new column.'''
    for dataframe in dataframes:
        FWBR_values = []
        if len(dataframe)<=500:
            for index, row in dataframe.iterrows():
                FWBR = -1 * (5.810 * log(row['CBO']+1,10)) + 3.112 * (log(row['DIT'] +1,10)) +0.067 * (log(row['WMC'] +1,10)) - 1.012 * (log(row['RFC']+1,10)) -0.041 * (log(row['LCOM']+1,10)) - 0.132 * (log(row['NOC']+1,10))
                FWBR_values.append(FWBR)
            dataframe["FWBR_s"]=FWBR_values
        if len(dataframe)>500 and len(dataframe)<1500:
            for index, row in dataframe.iterrows():
                FWBR = -1 * (9.023 * log(row['CBO']+1,10)) + 3.945 * (log(row['DIT'] +1,10)) -0.678 * (log(row['WMC'] +1,10)) - 0.826 * (log(row['RFC']+1,10)) -0.378 * (log(row['LCOM']+1,10))
                FWBR_values.append(FWBR)
            dataframe["FWBR_N"]=FWBR_values
        if len(dataframe)>=1500:
            for index, row in dataframe.iterrows():
                FWBR = -1 * (8.151 * log(row['CBO']+1,10)) + 1.431 * (log(row['DIT'] +1,10)) -2.788 * (log(row['WMC'] +1,10)) + 2.501 * (log(row['RFC']+1,10)) -0.191 * (log(row['LCOM']+1,10)) -1.242 * (log(row['NOC']+1,10))
                FWBR_values.append(FWBR)
            dataframe["FWBR_N"]=FWBR_values

calculate_FWBR(dataframes)
calculate_FWBR_subs(dataframes)

print(df_ck_55133.head())





