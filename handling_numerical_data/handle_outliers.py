import pandas as pd 
import numpy as np 


###############################################
# Elimination method to outlier handling      #
###############################################

houses = pd.DataFrame()
houses['Prices'] = [5000,2000,3000,6000]
houses['Bathrooms'] = [2,3,4,60]
# filter observations
new_dataframe = houses[houses['Bathrooms'] < 10]
print (new_dataframe)

#################################################
# Mark them as outliers and create a new feature#
#################################################

houses['Outlier'] = np.where(houses["Bathrooms"] < 10, 0,1)
print(houses)

#########################################################
# we can transform the feature to dampen outlier effect #
#########################################################
houses["Log_Of_Prices"] = [np.log(x) for x in houses["Prices"]]
print(houses)