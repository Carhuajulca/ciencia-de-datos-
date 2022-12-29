import numpy as np

A = np.array([[6,1], [2,-3], [-10,8]])
print("Dimención: ",A.ndim)
print(A)

print("")
b = np.array([[4, 0, 9], [-7, 2, -5]])
print("Dimención: ",b.ndim)
print()
print(np.transpose(b))

# X = np.linalg.solve( A, b )
# print(X)
