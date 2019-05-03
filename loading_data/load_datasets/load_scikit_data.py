# load scikit-learn's datasets
from sklearn import datasets

#load digits dataset
digits = datasets.load_digits()

# create features matrix

features = digits.data
print('feature matrix',features)

#create target vector
target = digits.target
print('target vector',target)
features[0]
print(features[0])