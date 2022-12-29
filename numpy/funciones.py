# Usando las funciones  con arrays
import numpy as np

data = np.array([2,3])
# exponente = np.power(data, 4)

# print(exponente)
datot = np.arange(24).reshape(4, 6)
# print(datot[0,3])
# print(datot)


# CONCATENANDO MATRICES 
m1 = np.array([1, 2, 3, 4])
m2 = np.array([5, 6, 7, 8])

# print(np.concatenate((m1, m2)))

# NÚMEROS ALIATORIOS  


# EJES AXIS = 0 > Y  AND AXIS = 1 > X
m = np.array([[ 1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
print("")
# minismo y maximos: amax and amin
print(np.amin(m, 1))