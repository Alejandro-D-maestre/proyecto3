
from pandas import Series
import numpy as np
import random

lista_aleatoria = [random.randint(1, 100) for _ in range(10)]
serie = Series(lista_aleatoria, index=range(1, 11), name="Numero aleatorio")
serie.index.name = "idx"
serie_cuadrados = serie ** 2
ultimos_4 = serie_cuadrados.tail(4)
mayores_500 = serie_cuadrados[serie_cuadrados > 500].tolist()

print("Lista aleatoria:", lista_aleatoria)
print("\nSerie original:\n", serie)
print("\nSerie de cuadrados:\n", serie_cuadrados)
print("\nÚltimos 4 elementos:\n", ultimos_4)
print("\nValores mayores a 500 (como lista):", mayores_500)
