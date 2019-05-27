import numpy as np 
from sklearn.preprocessing import FunctionTransformer

# create a feature
features = np.array([
    [2,3],
    [2,3],
    [2,3]
])

# define a simple function
def add_item(x):
    return x + 10

ten_transformer = FunctionTransformer(add_item)

# tranform feature matrix
t = ten_transformer.transform(features)
print(t)
