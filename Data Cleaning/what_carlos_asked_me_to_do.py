import pandas as pd

cis = pd.read_csv('FINAL_CIS.csv')

cis = cis[(cis['EFATINC'] > 0) & (cis['EFATINC'] < 40000) & (cis['YEAR'] != 2017)]

prov_year_group = cis.groupby(['PROV', 'YEAR', 'FSCHHLDM']).size().reset_index(name='count')

prov_year = cis.groupby(['PROV', 'YEAR']).size().reset_index(name='total')
percents = pd.merge(prov_year_group, prov_year, on=['PROV', 'YEAR'])
percents['percent'] = ((percents['count'] / percents['total']) * 100).round(1)

percents.to_csv("what_carlos_asked_me_to_do.csv")

print(percents)