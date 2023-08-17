#Herramientas y librerias necesarias poara el codigo y los graficos
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Carga de tabla desde el explorador de archivos

# Este codigo abre el administrador de archivos pero lo abre detras del VSC debe ser problema de tkinter ya que 
# con el solamente es que se presenta esa falla
# Crear una ventana de selección de archivo
### Version 2 final 

def load_data():
    # Crear una ventana de selección de archivo
    root = tk.Tk()
    root.withdraw()

    # Seleccionar el archivo XLSX o XLS con el Administrador de archivos
    file_path = filedialog.askopenfilename(filetypes=[
        ("Archivos Excel", "*.xlsx;*.xls")   
    ])

    if file_path:
        # Obtener la extensión del archivo seleccionado
        file_extension = file_path.split(".")[-1]

        if file_extension in ["xlsx", "xls"]:
            # Cargar el archivo XLSX o XLS en un DataFrame
            data = pd.read_excel(file_path)
        else:
            print("Formato de archivo no compatible.")
            return None

        if data is not None:
            # Ordenar el DataFrame por la columna "Resultado" de manera ascendente
            data = data.sort_values(by="Resultado")
            return data
        else:
            return None
    else:
        return None

# Ejemplo de cómo usar la función
loaded_data = load_data()
if loaded_data is not None:
    print(loaded_data)
