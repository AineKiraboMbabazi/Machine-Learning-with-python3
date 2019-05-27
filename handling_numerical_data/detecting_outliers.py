import numpy as np 
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs

# create simulated data
features,_ = make_blobs(n_samples=10, centers=1, n_features=2, random_state=1)
features[0,0] = 10000
features[0,1] = 10000
# create detectors
outlier_detector = EllipticEnvelope(contamination=.1)

# fit detector
outlier_detector.fit(features)

# predict outliers
w = outlier_detector.predict(features)
print(w)