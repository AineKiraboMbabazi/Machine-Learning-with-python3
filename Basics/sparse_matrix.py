import numpy as np
from scipy import sparse

matrix = np.array([[0,0],[0,1],[3,0],[4,0]])

#create compressed sparse row matrix
#sparse matrices only store non zero elements of and assume all other values will be zero


matrix_sparse =sparse.csr_matrix(matrix)
print (matrix_sparse)