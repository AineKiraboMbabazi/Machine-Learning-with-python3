import pandas as pd 

# load data
dataframe = pd.DataFrame()
dataframe['Name'] =['Aine Grace','Aine Grace','Mbabazi Mercy','Kirabo Gift',"test field"]
dataframe['Age'] = [23,23,24,22,30]
dataframe['Driver'] = [True,True, True,False,True]

def toUpperCase(y):
    return y.upper()

t = dataframe['Name'].apply(toUpperCase)[0:3]
print(t )
