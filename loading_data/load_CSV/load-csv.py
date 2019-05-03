import pandas as pd 

# define data source URL
url = 'http://www.cs.cmu.edu/~jernst/st/randomdatanoplants.txt'

# load dataset
dataframe = pd.read_csv(url)

# view first two rows 
dataframe.head()
print(dataframe.head(10))