import pandas as pd 

# load data
data_a = {
    'id': ['1', '2', '3'],
    'first': ['Alex', 'Amy', 'Allen'],
    'last': ['Anderson', 'Ackerman', 'Ali']
    }

dataframe_a = pd.DataFrame(data_a, columns = ['id', 'first', 'last'])

# Create DataFrame

data_b = {
    'id': ['4', '5', '6'],
    'first': ['Billy', 'Brian', 'Bran'],
    'last': ['Bonder', 'Black', 'Balwner']
    }

dataframe_b = pd.DataFrame(data_b, columns = ['id', 'first', 'last'])
# Concatenate DataFrames by rows
# axes parameter describe the way the data is represented
# if axes = 0

#  id  first      last
# 0  1   Alex  Anderson
# 1  2    Amy  Ackerman
# 2  3  Allen       Ali
# 0  4  Billy    Bonder
# 1  5  Brian     Black
# 2  6   Bran   Balwner

# if axes =1
#   id  first      last id  first     last
# 0  1   Alex  Anderson  4  Billy   Bonder
# 1  2    Amy  Ackerman  5  Brian    Black
# 2  3  Allen       Ali  6   Bran  Balwner
# print(pd.concat([dataframe_a, dataframe_b], axis=1))
