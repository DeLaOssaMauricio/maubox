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
root = tk.Tk()
root.withdraw()

 # Seleccionar el archivo XLSX o XLS con el Administrador de archivos
df = filedialog.askopenfilename(filetypes=[
        ("Archivos Excel", "*.xlsx;*.xls")   
    ])

def load_data(df):
    

    # Verificar si se seleccionó un archivo
    if df:
        # Obtener la extensión del archivo seleccionado
        file_extension = df.split(".")[-1]

        if file_extension in ["xlsx", "xls"]:
            # Cargar el archivo XLSX o XLS en un DataFrame
            data = pd.read_excel(df)
        else:
            print("Formato de archivo no compatible.")
            data = None

        if data is not None:
            # Ordenar el DataFrame por la columna "Resultado" de manera ascendente
            data = data.sort_values(by="Resultado")
            
            # Retorna el DataFrame ordenado
            return data
        else:
            return None
    else:
        return None


