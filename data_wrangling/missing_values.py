import pandas as pd 
import numpy as np 


# load data
dataframe = pd.DataFrame()
dataframe['Name'] =['Aine Grace','Mbabazi Mercy','Kirabo Gift'," "]
dataframe['Age'] = [23,24,22,30]
dataframe['Driver'] = [True, True,False,True]
dataframe['Driver'] = dataframe['Driver'].replace(False,np.nan)
print(dataframe)
print (dataframe[dataframe['Driver'].isnull()])