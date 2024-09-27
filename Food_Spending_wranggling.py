import pandas as pd

fs=pd.read_csv("Food Spending.csv")

#get all the columns name
list(fs.columns)

#remove the columns we do not need
fs=fs.drop(columns=['DGUID','Statistic','UOM_ID','SCALAR_FACTOR','SCALAR_ID','VECTOR','COORDINATE','STATUS','SYMBOL','TERMINATED','DECIMALS'])

#change column position and column name
fs=fs.rename(columns={'REF_DATE':'YEAR','GEO':'PROV', 'Food expenditures, summary-level categories':'Way_to_Spend','UOM':'Unit','VALUE':'Value'})
new_columns=['YEAR','PROV','Way_to_Spend','Value','Unit']
fs=fs[new_columns]

#remove data with year less than 2017
fs=fs.drop(fs[(fs['YEAR']<2017)].index)

#keep all the rows which are Food purchased from stores and resturant meals
fs=fs[(fs['Way_to_Spend']=='Food purchased from stores')|(fs['Way_to_Spend']=='Restaurant meals')|(fs['Way_to_Spend']=='Food expenditures')]

#Remove rows of Canada,Atlantic Region and Prairie Region and sort them
fs=fs.drop(fs[(fs['PROV']=='Canada')].index)
fs=fs.drop(fs[(fs['PROV']=='Atlantic Region')].index)
fs=fs.drop(fs[(fs['PROV']=='Prairie Region')].index)

#put year, province and Way to spend as multiindex
fs.set_index(['YEAR','PROV','Way_to_Spend'],inplace=True)

#Save as a new file
fs.to_csv("Cleaned_Food_Spending.csv")