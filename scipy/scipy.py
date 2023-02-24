
# import numpy as np
# A = np.array([[1,2,3],[4,5,6],[7,8,8]])

# from scipy import linalg

# linalg.det(A)
# eigen_values, eigen_vectors = linalg.eig(A)
# print(eigen_values)
# print(eigen_vectors)

from scipy import integrate
f = lambda y, x: x*y**2
i = integrate.dblquad(f, 0, 2, lambda x: 0, lambda x: 1)
# print the results
print(i)
