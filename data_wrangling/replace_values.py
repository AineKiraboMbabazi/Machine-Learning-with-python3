import pandas as pd 

# create dataframe
dataframe = pd.DataFrame()

# add columns
dataframe['Name'] =['Aine Grace','Mbabazi Mercy','Kirabo Gift']
dataframe['Age'] = [23,24,22]
dataframe['Driver'] = [True, True,False]

# print(dataframe['Name'].replace(['Aine Grace','Aine Kirabo']).head(3))
y = dataframe.replace(True,'1').head(3)
p = dataframe.replace(False,'0').head(3)
print(y)
print(p)