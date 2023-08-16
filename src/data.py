import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

root = tk.Tk()
root.withdraw()


def load_data(file_path):
    
    file_path = filedialog.askopenfilename(filetypes=[
        
        ("Archivos Excel", "*.xlsx;*.xls")
    ])   

    # Verificar si se seleccionó un archivo
    if file_path:
            # Obtener la extensión del archivo seleccionado
            file_extension = file_path.split(".")[-1]

            
            if file_extension in ["xlsx", "xls"]:
                # Cargar el archivo XLSX o XLS en un DataFrame
                data = pd.read_excel(file_path)
            else:
                print("Formato de archivo no compatible.")
                data = None

            if data is not None:
                # Ordenar el DataFrame por la columna "Resultado" de manera ascendente
                data_sorted1 = data.sort_values(by="Resultado")

    return(data_sorted1)   