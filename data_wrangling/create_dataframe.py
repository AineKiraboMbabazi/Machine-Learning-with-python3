import pandas as pd 

# create dataframe
dataframe = pd.DataFrame()

# add columns
dataframe['Name'] =['Aine Grace','Mbabazi Mercy','Kirabo Gift']
dataframe['Age'] = [23,24,22]
dataframe['Driver'] = [True, True,False]

# print(dataframe)

# adding a row to an existent dataframe
new_entry = pd.Series(['Kembabazi Tracy',20,True ], index = ['Name','Age','Driver'])
test = dataframe.append(new_entry, ignore_index= True)
print(test)