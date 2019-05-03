import numpy as np 

# create a 2D matrix
matrix = np.array([[1,4],[2,5],[3,6]])

#create function that adds 100 to something
add_100 = lambda i : i+100

#create vectorized function
vectorized_add_100 = np.vectorize(add_100)

#apply function to all elements in the matrix
result = vectorized_add_100(matrix)
print(matrix.reshape(2,3))
print('transpose')
print(matrix.T)
print (result, np.average(matrix), np.min(matrix), np.max(matrix),np.mean(matrix,axis=0), np.std(matrix),np.var(matrix))