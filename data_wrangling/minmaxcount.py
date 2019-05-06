import pandas as pd 


# load data
dataframe = pd.DataFrame()
dataframe['Name'] =['Aine Grace','Mbabazi Mercy','Kirabo Gift']
dataframe['Age'] = [23,24,22]
dataframe['Driver'] = [True, True,False]

print('maximum :',dataframe['Age'].max())
print('minimum :',dataframe['Age'].min())
print('Mean :',dataframe['Age'].mean())
print('Count :',dataframe['Age'].count())
