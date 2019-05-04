import pandas as pd 
import collections
# create dataframe
dataframe = pd.DataFrame()

# add columns
dataframe['Name'] =['Aine Grace','Mbabazi Mercy','Kirabo Gift']
dataframe['Age'] = [23,24,22]
dataframe['Driver'] = [True, True,False]
new = dataframe.rename(columns={'Name':'Full_Name'}).head()
print(new)

# creating a dictionary of dataset column names
column_names = collections.defaultdict(str)
for name in dataframe.columns:
    column_names[name]

print(column_names)