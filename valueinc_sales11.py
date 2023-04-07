# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 23:42:41 2023

@author: smith
"""

import pandas as pd


data=pd.read_csv('transaction.csv', sep =';')
costperitem=data['CostPerItem']
numberofitemspurchased=data['NumberOfItemsPurchased']
costpertransaction= numberofitemspurchased * costperitem
data['costpertransaction']=data['CostPerItem'] * data['NumberOfItemsPurchased']
data['salepertransaction']= data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['profitpertransaction']=data['salepertransaction']  - data['costpertransaction']

data['markup']= (data['salepertransaction']  - data['costpertransaction']) /data['costpertransaction']  
data['markup']=round(data['markup'],2) 

data['day']=data['Day'].astype(str) +'- '+ data['Month'].astype(str)+'- '+ data['Year'].astype(str)

#split a clumn
split_column= data['ClientKeywords'].str.split( ',' ,  expand=True )
data['ClientAge']=split_column[0]
data['ClientType']=split_column[1]
data['LengthofContract']=split_column[2]

#replace a column
data['ClientAge']=data['ClientAge'].str.replace('[' , '')
data['LengthofContract']=data['LengthofContract'].str.replace(']' , '')


#change to lowercase
data['ItemDescription']=data['ItemDescription'].str.lower()

#merging datasets
seasons = pd.read_csv('value_inc_seasons.csv', sep =';')
data= pd.merge(data, seasons, on ='Month')

#dropping a column

data= data.drop('ClientKeywords' ,axis = 1)

# export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)
