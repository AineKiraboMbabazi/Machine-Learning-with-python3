import numpy as np 
import pandas as pd 
# first method uses numpy

# create a feature matrix
features = np.array([[1.1,11.1],[2.2,22.2],[np.nan,55.5]])

# keep only observations that are not missing
filtered_array = features[~np.isnan(features).any(axis=1)]
print(filtered_array)

# second method uses pandas
# convert the numpy array into a dataframe
dataframe = pd.DataFrame(features, columns=["feature_1","feature_2"])

# remove the mising values
new = dataframe.dropna()
print (new)