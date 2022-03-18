import pandas as pd
import csv
import math

df_ck_506 = pd.read_csv('results/ckjm/ckjm_5.0.6.csv')
df_ck_513 = pd.read_csv('results/ckjm/ckjm_5.1.3.csv')
df_ck_521 = pd.read_csv('results/ckjm/ckjm_5.2.1.csv')
df_ck_534 = pd.read_csv('results/ckjm/ckjm_5.3.4.csv')
df_ck_545 = pd.read_csv('results/ckjm/ckjm_5.4.5.csv')
df_ck_55133 = pd.read_csv('results/ckjm/ckjm_5.5.13.3.csv')


dataframes = [df_ck_506,df_ck_513,df_ck_521,df_ck_534,df_ck_545,df_ck_55133]
for dataframe in dataframes:
    FWBR_values = []
    for index, row in dataframe.iterrows():
        FWBR = -1 * (8.753 * math.log(row['CBO']+1)) + 2.505 * (math.log(row['DIT'] + 1)) - 1.922 * (math.log(row['WMC'] + 1)) + 0.89
        FWBR_values.append(FWBR)
    dataframe["FWBR"]=FWBR_values

print(df_ck_506.head())





