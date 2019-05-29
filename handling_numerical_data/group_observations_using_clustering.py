import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# make simulated feature matrix
features, _ =make_blobs(n_samples=50,n_features=2,centers=3,random_state=1)
 
# create a dataframe
df = pd.DataFrame(features, columns=["feature_1", "feature_2"])

# make k-means clusterer
clusterer = KMeans(3, random_state=0)

# fit clusterer
clusterer.fit(features)

# predict values

df["group"] = clusterer.predict(features)

# view first few observations
print (df.head(5))