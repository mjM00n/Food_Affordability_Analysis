import numpy as np
import pandas as pd

# # Load the datasets into python
files = [
    "Canadian Income Survey, 2017.xlsx",
    "Canadian Income Survey, 2018.xlsx",
    "Canadian Income Survey, 2019.xlsx",
    "Canadian Income Survey, 2020.xlsx",
    "Canadian Income Survey, 2021.xlsx"
]
# Converting files into dataframes
dfs = [pd.read_excel(file) for file in files]

# using 2017 dataset to define order of columns
clms = dfs[0].columns.tolist()

# Rearranging columns to match 2017 dataset
for i, df in enumerate(dfs):
    dfs[i] = df[clms]

# Stacking datasets
combined_data = pd.concat(dfs, ignore_index=True)

# Sorting By using column "YEAR"
combined_data['YEAR'] = combined_data['YEAR'].astype(int)
combined_data = combined_data.sort_values(by='YEAR')

# updating values of columns that is hard to understand, i.e, Province no's to names
combined_data['PROV'] = combined_data['PROV'].replace(
    [10, 11, 12, 13, 24, 35, 46, 47,
     48, 59, 60, 61, 62, 96, 97, 98, 99],
    ["Newfoundland and Labrador",
     "Prince Edward Island",
     "Nova Scotia", "New Brunswick",
     "Quebec", "Ontario", "Manitoba",
     "Saskatchewan", "Alberta",
     "British Columbia","NaN","NaN",
     "NaN","NaN","NaN","NaN","NaN"], inplace=True)

# combined_data = combined_data["PROV"].replace(p_names).where(combined_data["PROV"].isin(p_names.keys()), np.nan)



# Deleting the MBM Region data
combined_data = combined_data.drop(columns= ['MBMREGP'])

# Deleting Duplicates
combined_data = combined_data.drop_duplicates()

combined_data.to_csv("FINAL_CIS")