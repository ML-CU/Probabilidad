import numpy as np
dados = [1, 2, 3, 4, 5, 6]
lanzamientos = 100000
acum = 0
resultados = []
for _ in range(lanzamientos):
    numeros = np.random.choice(dados)
    resultados.append(numeros)

print(sum(resultados)/lanzamientos)