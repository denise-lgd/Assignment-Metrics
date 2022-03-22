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

#load layer extractor results
df_le_506 = pd.read_csv("results/layer_extractor/le-metrics-5.0.6.csv", encoding='UTF-16 LE')
df_le_513 = pd.read_csv("results/layer_extractor/le-metrics-5.1.3.csv", encoding='UTF-16 LE')
df_le_521 = pd.read_csv("results/layer_extractor/le-metrics-5.2.1.csv", encoding='UTF-16 LE')
df_le_534 = pd.read_csv("results/layer_extractor/le-metrics-5.3.4.csv", encoding='UTF-16 LE')
df_le_545 = pd.read_csv("results/layer_extractor/le-metrics-5.4.5.csv", encoding='UTF-16 LE')
df_le_55133 = pd.read_csv("results/layer_extractor/le-metrics-5.5.13.3.csv", encoding='UTF-16 LE')

#make list of dataframes to loop over
le_dataframes = [df_le_506, df_le_513, df_le_521, df_le_534, df_le_545, df_le_55133]
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
            dataframe["FWBR_L"]=FWBR_values

calculate_FWBR(dataframes)
calculate_FWBR_subs(dataframes)

#print(df_ck_55133.head())

csv_names = ['506_results.csv','513_results.csv','521_results.csv','534_results.csv','545_results.csv','55133_results.csv', ]

# Align and merge data and output results
for i in range(len(le_dataframes)):
    df = dataframes[i]
    le_df = le_dataframes[i]
    for index, row in df.iterrows():
        layer = le_df[le_df["ClassName"] == row["ClassName"]]["layer"].values[0]
        df.at[index, "layer"] = layer
    df.to_csv('./results/' + csv_names[i])


for i in range(len(dataframes) - 1):
    version_name_a = csv_names[i]
    version_name_b = csv_names[i+1]

    version_a = dataframes[i]
    version_b = dataframes[i+1]

    le_a = le_dataframes[i]
    le_b = le_dataframes[i+1]

    no_changes_fwbr = 0
    no_changes_layer = 0

    # Calculate fwbr changes
    for index, row in version_a.iterrows():
        fwbr_a = row['FWBR']
        fwbr_b_entries = version_b[version_b["ClassName"] == row["ClassName"]]["FWBR"]


        if len(fwbr_b_entries.values) > 0:
            if fwbr_a != fwbr_b_entries.values[0]:
                no_changes_fwbr += 1

    print(version_name_a, version_name_b, no_changes_fwbr)

    # Calculate layer changes
    for index, row in le_a.iterrows():
        layer_a = row['layer']
        layer_b_entries = le_b[le_b["ClassName"] == row["ClassName"]]["layer"]

        if len(layer_b_entries.values) > 0:
            if  layer_a != layer_b_entries.values[0]:
                no_changes_layer += 1
    print(version_name_a, version_name_b, no_changes_layer)

 
#calculating min/max values for quiz question 2:
for dataframe in dataframes:
    min_max_values = {}
    for column in ['WMC','DIT','NOC','CBO','RFC','LCOM','CA','NPM']:
        min_max_values[column] = [min(dataframe[column]),max(dataframe[column])]
    print(min_max_values)
for dataframe in le_dataframes:
    print(min(dataframe['layer']), max(dataframe['layer']))