import pandas as pd 

# create JSON data source url
url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'

# load data
dataframe = pd.read_json(url,orient='rows')

print(dataframe.head())