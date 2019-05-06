import pandas as pd 

# load data
dataframe = pd.DataFrame()
dataframe['Name'] =['Aine Grace','Aine Grace','Mbabazi Mercy','Kirabo Gift',"test field"]
dataframe['Age'] = [23,23,24,22,30]
dataframe['Driver'] = [True,True, True,False,True]
print(dataframe)
drop_duplicate_rows = dataframe.drop_duplicates()
print(drop_duplicate_rows)