import pandas as pd
import csv
from math import log
import matplotlib.pyplot as plt


df_results_506 = pd.read_csv('results/506_results.csv')
df_results_513 = pd.read_csv('results/513_results.csv')
df_results_521 = pd.read_csv('results/521_results.csv')
df_results_534 = pd.read_csv('results/534_results.csv')
df_results_545 = pd.read_csv('results/545_results.csv')
df_results_55133 = pd.read_csv('results/55133_results.csv')

result_dataframes = [df_results_506,df_results_513,df_results_521,df_results_534,df_results_545,df_results_55133]

fwbr_changes = []
layer_changes = []

for i in range(len(result_dataframes) - 1):

    version_a = result_dataframes[i]
    version_b = result_dataframes[i+1]

    fwbr_changes_transition = []
    layer_changes_transition = []

    # Calculate layer changes
    for index, row in version_a.iterrows():
        layer_a = row['layer']
        layer_b_entries = version_b[version_b["ClassName"] == row["ClassName"]]["layer"]
        fwbr_a = row['FWBR']
        fwbr_b_entries = version_b[version_b["ClassName"] == row["ClassName"]]["FWBR"]

        if len(layer_b_entries.values) > 0:
            if  layer_a != layer_b_entries.values[0]:
                layer_change = layer_a - layer_b_entries.values[0]
                fwbr_change = fwbr_a - fwbr_b_entries.values[0]
                fwbr_changes_transition.append(fwbr_change)
                layer_changes_transition.append(layer_change)
    
    fwbr_changes.append(fwbr_changes_transition)
    layer_changes.append(layer_changes_transition)

fig, ax = plt.subplots(2,3)
ax[0,0].scatter(layer_changes[0], fwbr_changes[0])
ax[0,0].set_title('5.0.6 to 5.1.3')
ax[0,0].axvline(c='r')
ax[0,0].axhline(c='r')
ax[0,1].scatter(layer_changes[1], fwbr_changes[1])
ax[0,1].set_title('5.1.3 to 5.2.1')
ax[0,1].axvline(c='r')
ax[0,1].axhline(c='r')
ax[0,2].scatter(layer_changes[2], fwbr_changes[2])
ax[0,2].set_title('5.2.1 to 5.3.4')
ax[0,2].axvline(c='r')
ax[0,2].axhline(c='r')
ax[1,0].scatter(layer_changes[3], fwbr_changes[3])
ax[1,0].set_title('5.3.4 to 5.4.5')
ax[1,0].axvline(c='r')
ax[1,0].axhline(c='r')
ax[1,1].scatter(layer_changes[4], fwbr_changes[4])
ax[1,1].set_title('5.4.5 to 5.5.13.3')
ax[1,1].axvline(c='r')
ax[1,1].axhline(c='r')
fig.text(0.5, 0.04, 'Change in layers (version 1 - version 2)', ha='center')
fig.text(0.04, 0.5, 'Change in FWBR (version 1 - version 2)', va='center', rotation='vertical')
plt.show()

print(len(layer_changes[0]))

