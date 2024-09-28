import pandas as pd

fs = pd.read_csv("Food Spending.csv")

# get all the columns name
list(fs.columns)

# remove the columns we do not need
fs = fs.drop(columns=['DGUID', 'Statistic', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS'])

<<<<<<< HEAD
# change column position and column name
fs = fs.rename(columns={'REF_DATE': 'Year', 'GEO': 'Province', 'Food expenditures, summary-level categories': 'Way_to_Spend', 'UOM': 'Unit', 'VALUE': 'Value'})
new_columns = ['Year', 'Province', 'Way_to_Spend', 'Value', 'Unit']
fs = fs[new_columns]

# Remove data with year less than 2017 (you had two different conditions in the conflict)
fs = fs.drop(fs[(fs['Year'] < 2017)].index)
=======
#change column position and column name
fs=fs.rename(columns={'REF_DATE':'YEAR','GEO':'PROV', 'Food expenditures, summary-level categories':'Way_to_Spend','UOM':'Unit','VALUE':'Value'})
new_columns=['YEAR','PROV','Way_to_Spend','Value','Unit']
fs=fs[new_columns]

#remove data with year less than 2017
fs=fs.drop(fs[(fs['YEAR']<2017)].index)
>>>>>>> 72d09037f561f7600dd7bae56bc99681274c5a3a

# keep all the rows which are Food purchased from stores and restaurant meals
fs = fs[(fs['Way_to_Spend'] == 'Food purchased from stores') | (fs['Way_to_Spend'] == 'Restaurant meals') | (fs['Way_to_Spend'] == 'Food expenditures')]

<<<<<<< HEAD
# Remove rows of Canada, Atlantic Region, and Prairie Region and sort them
fs = fs.drop(fs[(fs['Province'] == 'Canada')].index)
fs = fs.drop(fs[(fs['Province'] == 'Atlantic Region')].index)
fs = fs.drop(fs[(fs['Province'] == 'Prairie Region')].index)

# Put year, province, and Way to spend as multi-index
fs.set_index(['Year', 'Province', 'Way_to_Spend'], inplace=True)
=======
#Remove rows of Canada,Atlantic Region and Prairie Region and sort them
fs=fs.drop(fs[(fs['PROV']=='Canada')].index)
fs=fs.drop(fs[(fs['PROV']=='Atlantic Region')].index)
fs=fs.drop(fs[(fs['PROV']=='Prairie Region')].index)

#put year, province and Way to spend as multiindex
fs.set_index(['YEAR','PROV','Way_to_Spend'],inplace=True)
>>>>>>> 72d09037f561f7600dd7bae56bc99681274c5a3a

# Save as a new file
fs.to_csv("Cleaned_Food_Spending.csv")

print(fs)