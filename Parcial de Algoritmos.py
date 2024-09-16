import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ruta_archivo_excel = "C:/Algoritmos 2/Cuestionario de algoritmos 2(1-20).xlsx"
df_excel = pd.read_excel(ruta_archivo_excel)

# Especificar las columnas que quieres graficar usando los títulos
columnas_a_graficar = ['¿Qué día de la semana madruga mas?', '¿Cuál es el pais mas grande del mundo?', 
'¿que tan feliz se siente?', '¿Cuál es su fecha de nacimiento?', 'organizar de la unidad de medida mas pequeña arriba a la mas grande abajo',
'le agrada su ambiente laboral o universitario', 'le agrada el grupo de amigos con el que convive']

for columna in columnas_a_graficar:
    datos = df_excel[columna].values
    plt.figure()
    plt.plot(datos, marker='o', linestyle='-', color=np.random.rand(3,))
    plt.title(f'Gráfico de la columna {columna}')
    plt.xlabel('Índice')
    plt.ylabel(columna)
    plt.show()
