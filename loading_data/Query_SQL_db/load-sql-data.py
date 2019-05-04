import pandas as pd 
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine


# create a connection to the database
# db = 'myfarm_test'
#             if os.getenv('APP_SETTINGS') == 'testing':
#                 db = 'test_db'
#             self.con_parameter = dict(
# #                 database=db,
# #                 user="root",
# #                 password="",
# #                 host="localhost"
# #             )
# DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"

# engine = create_engine(DB_URI.format(
#   user ='root',
#   password = '',
#   host = 'localhost',
#   port = '8080',
#   db = 'myfarm_test',
#   connect_args = {'time_zone': '+00:00'}
#   )

# # load data
# # myquery = "SELECT * FROM animal"
# dataframe = pd.read_sql_query("SELECT * FROM animal",engine)

# print (dataframe.head())

# Create the db engine
engine = create_engine('sqlite:///:memory:')
# define data source URL
url = 'http://www.cs.cmu.edu/~jernst/st/randomdatanoplants.txt'

# load dataset
data = pd.read_csv(url)
# Store the dataframe as a table
data.to_sql('data_table', engine)

# Query 1 on the relational table
res1 = pd.read_sql_query('SELECT * FROM data_table', engine)
print('Result 1')
print(res1)