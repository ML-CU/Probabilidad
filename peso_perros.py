import numpy as np
promedio = 60 #promedio real (miu)
desv_std = 3
pop = np.random.normal(loc=promedio, scale=desv_std, size = 1034)

trials = 100 #numero de veces que se sacará el promedio muestral
medias = []
n_size = 20 #numero de perros por muestra
for _ in range(trials):
    medias.append(np.random.choice(pop, n_size).mean()) #peso promedio de los perros de cada muestra
print(sum(medias)/trials) #Determinamos el promedio de las muestras, y el resultado mostrara muy cercano a 60