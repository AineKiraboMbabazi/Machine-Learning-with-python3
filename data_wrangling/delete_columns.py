import pandas as pd 



# load data
dataframe = pd.DataFrame()
dataframe['Name'] =['Aine Grace','Mbabazi Mercy','Kirabo Gift'," "]
dataframe['Age'] = [23,24,22,30]
dataframe['Driver'] = [True, True,False,True]
print(dataframe.drop('Driver', axis=1).head(3))