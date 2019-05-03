import numpy as np

# create a 2D matrix
matrix = np.array([[1,4],[2,5],[3,6]])

#create a vector as a row
vector = np.array([1,2,3])

print( vector[-1])
print (matrix[1,1])
print (matrix[:1, :])
print(matrix.shape)