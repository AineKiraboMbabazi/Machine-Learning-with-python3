import numpy as np 
from sklearn.preprocessing import Binarizer
# Binarize the feature according to some threshold

# create feature
age = np.array([[6],[12],[20],[36],[65]])

# create binarizer
binarizer = Binarizer(18)

# transform feature
b = binarizer.fit_transform(age)
print(b)

# Breakup the numerical features according to multiple thresholds

# bin feature
new= np.digitize(age, bins=[20,30,64])
print(new)