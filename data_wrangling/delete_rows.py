import pandas as pd 

# load data
dataframe = pd.DataFrame()
dataframe['Name'] =['Aine Grace','Mbabazi Mercy','Kirabo Gift',"test field"]
dataframe['Age'] = [23,24,22,30]
dataframe['Driver'] = [True, True,False,True]
delete_test_field = dataframe[dataframe['Driver'] == False]
print(delete_test_field.head(3))
print(dataframe)