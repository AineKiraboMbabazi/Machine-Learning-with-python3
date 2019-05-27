import numpy as np 
from sklearn.preprocessing import PolynomialFeatures

# create feature matrix
features = np.array([
    [2,3],
    [2,3],
    [2,3]
])

# create PolynomialFeatures object
polynomial_interaction = PolynomialFeatures(degree=3, include_bias=False)

# create polynomial function
p = polynomial_interaction.fit_transform(features)
print(p)