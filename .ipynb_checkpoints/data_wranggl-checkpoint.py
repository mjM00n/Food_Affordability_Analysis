import pandas as pd

# Load the datasets into python
files = [
    "Canadian Income Survey, 2018.xlsx",
    "Canadian Income Survey, 2019.xlsx",
    "Canadian Income Survey, 2020.xlsx",
    "Canadian Income Survey, 2021.xlsx"
]

# Converting files into dataframes
dfs = [pd.read_excel(file) for file in files]

# using 2018 dataset to define order of columns
clms = dfs[0].columns.tolist()

# Rearranging columns to match 2018 dataset
for i, df in enumerate(dfs):
    dfs[i] = df[clms]

# Stacking datasets
combined_data = pd.concat(dfs, ignore_index=True)

# Sorting By using column "YEAR"
combined_data['YEAR'] = combined_data['YEAR'].astype(int) # Convert to int if necessary
combined_data = combined_data.sort_values(by='YEAR')

# saving the combined data set
combined_data.to_excel("Combined_Canadian_Income_Survey.xlsx", index=False)

# Shortening the notation of the combined data set
cis = pd.read_excel("Combined_Canadian_Income_Survey.xlsx")

# Changing provincial data in the combined data to strings
cis.PROV.replace([10, 11, 12, 13, 24, 35, 46, 47, 48, 59, 60, 61, 62, 96, 97, 98, 99], ["Newfoundland and Labrador","Prince Edward Island","Nova Scotia","New Brunswick","Quebec","Ontario","Manitoba","Saskatchewan","Alberta","British Columbia","Yukon","Northwest Territories","Nunavut","NaN","NaN","NaN","NaN"])
