import pandas as pd

url = '/home/mbabazi/airline.xls' 

# load data 
dateframe = pd.read_excel(url,name=0 , header=1)

print(dateframe.head(10))
