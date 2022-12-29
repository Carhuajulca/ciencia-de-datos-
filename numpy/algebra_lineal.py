# ALGEBRA LINEAL 
import numpy as np

A = np.array([[2,1,-2], [3,0,1], [1,1,-1]])

print("Dimención: ",A.ndim)
print(A)
print("")

B = np.array([[-3], [5], [-2]])
print("Dimención: ",B.ndim)
# print(B)
print("")
print("Transponiendo")
print(B)
print("")

X = np.linalg.solve(A,B)
print(X)

