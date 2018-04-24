import numpy as np

altura = [1.72, 1.56, 1.45, 1.76, 1.68]
peso   = [86.5, 56.6, 70.4, 80.8, 90.7]

nAltura = np.array(altura)
nPeso = np.array(peso)
imc = nPeso / nAltura ** 2

print(imc)
