import pandas as pd 
from sqlalchemy import create_engine


# create a connection to the database
dbcon = create_engine('sqlite:///sample.db')

# load data
dataframe = pd.read_sql_query('SELECT * FROM data',dbcon)

print (dataframe.head())