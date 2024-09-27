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
p_names = {
    10: "Newfoundland and Labrador",
    11: "Prince Edward Island",
    12: "Nova Scotia",
    13: "New Brunswick",
    24: "Quebec",
    35: "Ontario",
    46: "Manitoba",
    47: "Saskatchewan",
    48: "Alberta",
    59: "British Columbia"
}

combined_data = combined_data["PROV"].replace(p_names).where(combined_data["PROV"].isin(p_names.keys()), np.nan)

# Deleting the rows that have missing values
combined_data = combined_data.dropna()

# Deleting Duplicates
combined_data = combined_data.drop_duplicates()

combined_data.to_csv("FINAL_CIS")