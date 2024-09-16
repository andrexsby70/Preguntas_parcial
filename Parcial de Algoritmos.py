import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Toplevel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Cargar el archivo de Excel
excel = "C:/algoritmos_2_parcial/Cuestionario.xlsx"
data_frame = pd.read_excel(excel)

# Lista de columnas
columnas = ['¿Qué día de la semana madruga mas?', '¿Cuál es el pais mas grande del mundo?',
            '¿que tan feliz se siente?', '¿Cuál es su fecha de nacimiento?', 
            'ordene de menor a mayor las medidas',
            '¿le agrada su ambiente laboral?', 
            '¿le agrada su grupo social?', '¿Es probable que madrugue un domingo?']

# Función para mostrar el gráfico en una nueva ventana
def mostrar_grafico_en_ventana(columna):
    # Crear una nueva ventana
    ventana_grafico = Toplevel()
    ventana_grafico.title(f'Gráfico - {columna}')
    
    # Obtener los datos de la columna seleccionada
    datos = data_frame[columna].values
    
    # Limpiar la figura anterior
    plt.clf()
    
    # Crear el gráfico
    plt.plot(datos, marker='o', linestyle='-', color=np.random.rand(3,))
    plt.title(f'Gráfico de la columna {columna}')
    plt.xlabel('Índice')
    plt.ylabel(columna)
    
    # Mostrar el gráfico en la nueva ventana de Tkinter
    canvas = FigureCanvasTkAgg(plt.gcf(), master=ventana_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Crear la ventana principal
ventana_principal = Tk()
ventana_principal.title("Gráficos de columnas")

# Etiqueta de introducción
label = Label(ventana_principal, text="Selecciona una columna para graficar:")
label.grid(row=0, column=0, columnspan=2, pady=10)

# Crear los botones en una cuadrícula de 2 columnas y 3 filas
for idx, columna in enumerate(columnas):
    fila = idx // 2  # Dividir el índice por 2 para obtener la fila
    columna_pos = idx % 2  # El resto de la división para obtener la columna (0 o 1)
    boton = Button(ventana_principal, text=columna, width=30, command=lambda c=columna: mostrar_grafico_en_ventana(c))
    boton.grid(row=fila+1, column=columna_pos, padx=10, pady=10)

# Iniciar la interfaz gráfica
ventana_principal.mainloop()
