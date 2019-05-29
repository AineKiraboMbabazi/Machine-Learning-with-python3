import numpy as np 
# from fancyimpute import KNN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs
# ######################################## #
#      Using K-nearest neighbor            #
# ######################################## #
# create a feature matrix
features,_=make_blobs(n_samples= 1000, n_features=2,random_state=1)

# standardize the features
scalar = StandardScaler()
standardized_features = scalar.fit_transform(features)
# replace the first features first value with a missing value
true_value = standardized_features[0,0]
standardized_features[0,0] = np.nan

# predict the missing values in the feature matrix
features_knn_imputed = KNN(k =5,verbose=0).complete(standardized_features)
# compare true and imputed values
print("true value : ", true_value)
print("Imputed value : ", features_knn_imputed[0,0])

# ######################################## #
#      Using scikit-learn's Imputer        #
# ######################################## #
from sklearn.preprocessing import Imputer
# create imputer
mean_imputer = Imputer(strategy="mean", axis=0)
# impute values
features_mean_imputed = mean_imputer.fit_transform(features)
# compare true and imputed values
print("True Value: ",true_value)
print("Imputed value: ", features_mean_imputed[0,0])