import numpy as np 
from sklearn import preprocessing

# create feature
feature = np.array ([
    [-500.5],
    [-100.1],
    [0],
    [100.1],
    [900.9]
])

# create scalar
minmax_scale = preprocessing.StandardScaler()

# scale feature
scaled_feature = minmax_scale.fit_transform(feature)
print(scaled_feature)
