# load library 
from sklearn.datasets import make_regression

# Generate features matrix, target vector, and the true coefficients
features, target, coefficients = make_regression(
    n_samples = 100,
    n_features = 3,
    n_informative = 3,
    n_targets = 1,
    noise = 0.0,
    coef = True,
    random_state = 1
    )


#view feature matrix and target vector
print(' feature matrix', features[:3])
print('target vector', target[:3])
print ('coefficients',coefficients)