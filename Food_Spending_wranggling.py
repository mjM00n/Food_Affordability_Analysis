import pandas as pd

fs=pd.read_csv("Food Spending.csv")

#get all the columns name
list(fs.columns)

#remove the columns we do not need
fs=fs.drop(columns=['DGUID','Statistic','UOM_ID','SCALAR_FACTOR','SCALAR_ID','VECTOR','COORDINATE','STATUS','SYMBOL','TERMINATED','DECIMALS'])

#change column position and column name
fs=fs.rename(columns={'REF_DATE':'Year','GEO':'Province', 'Food expenditures, summary-level categories':'Way_to_Spend','UOM':'Unit','VALUE':'Value'})
new_columns=['Year','Province','Way_to_Spend','Value','Unit']
fs=fs[new_columns]

#remove data with year less than 2018
fs=fs.drop(fs[(fs['Year']<=2018)].index)

#keep all the rows which are Food purchased from stores and resturant meals
fs=fs[(fs['Way_to_Spend']=='Food purchased from stores')|(fs['Way_to_Spend']=='Restaurant meals')|(fs['Way_to_Spend']=='Food expenditures')]

#Remove rows of Canada and Atlantic Region and sort them
fs=fs.drop(fs[(fs['Province']=='Canada')].index)
fs=fs.drop(fs[(fs['Province']=='Atlantic Region')].index)

#put year, province and Way to spend as multiindex
fs.set_index(['Year','Province','Way_to_Spend'],inplace=True)

#Save as a new file
fs.to_csv('Cleaned_Food_Spending.csv')