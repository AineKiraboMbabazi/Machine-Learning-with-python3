import pandas as pd 
import numpy as np 

# Create date range
time_index = pd.date_range('06/06/2017', periods=100000, freq='30S')

# Create DataFrame
dataframe = pd.DataFrame(index=time_index)

# Create column of random values
dataframe['Sale_Amount'] = np.random.randint(1, 10, 100000)

# Group rows by week, calculate sum per week
new_frame = dataframe.resample('W').sum()
print(new_frame)
new_frame1 = dataframe.resample('Y').sum()
print(new_frame1)