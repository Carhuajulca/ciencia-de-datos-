import numpy as np

# Coeficientes de las variables en las dos ecuaciones
coeffs_1 = [5, -1]
coeffs_2 = [5, -3]

# Lado derecho de las ecuaciones
rhs_1 = 14
rhs_2 = -9

# Resuelve el sistema de ecuaciones
a, x = np.linalg.solve([coeffs_1, coeffs_2], [rhs_1, rhs_2])

print(f"a = {a}, x = {x}")
