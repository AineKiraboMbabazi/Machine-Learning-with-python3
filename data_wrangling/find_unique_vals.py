import pandas as pd 


# load data
dataframe = pd.DataFrame()
dataframe['Name'] =['Aine Grace','Mbabazi Mercy','Kirabo Gift']
dataframe['Age'] = [23,24,22]
dataframe['Driver'] = [True, True,False]
print(dataframe['Name'].unique())
print(dataframe['Name'].value_counts())