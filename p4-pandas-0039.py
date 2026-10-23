import pandas as pd
import numpy as np
# Caleb Dorado NC = 0039
n_filas=5
n_columnas=5
tag_columna= tuple('ABCDE') # Etiquetas para las columnas de una tupla
print(tag_columna)
matriz=np.random.randint(1, 6, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("Con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# La variable df es DataFrame
df = pd.DataFrame(matriz, columns= tag_columna)
print(" --- La tabla o dataframe --- NC = 0039")
print(df)
print("--- Caleb Dorado NC = 0039 ---")