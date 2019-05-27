import numpy as np 
from sklearn.preprocessing import Normalizer

features = np.array([
    [0.5, 0.5],
    [1.1,3.4],
    [1.5,20.2],
    [1.63,34.4],
    [10.9,3.3]
])

# create Normalizer
Normalizer = Normalizer(norm='l2')

# transform feature matrix
normalised_data = Normalizer.transform(features)

print (normalised_data)