#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Carga de tabla desde el explorador de archivos

# In[107]:


# Crear una ventana de selección de archivo
root = tk.Tk()
root.withdraw()

# Seleccionar el archivo XLSX o XLS con el Administrador de archivos
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
        data_sorted = data.sort_values(by="Resultado")


# Medida de tendencia centra (Media, DS y CV) Antes de aplicar los filtros

# In[74]:


# Calcular la media, el coeficiente de variación (CV) y la variación estándar de la columna "Resultado"
media = data_sorted["Resultado"].mean()
ds = data_sorted["Resultado"].std()
cv = (data_sorted["Resultado"].std() / media) * 100  # Coeficiente de variación en porcentaje


print(f"Media: {media:.2f}")
print(f"Variación Estándar: {ds:.2f}")
print(f"Coeficiente de Variación (CV): {cv:.2f}%")



# In[102]:


tabla_grubbs = pd.DataFrame(
    {
        "N":[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 
        "ALFA 0.01":[2.4822, 2.5642, 2.6362, 2.6992, 2.7552, 2.8062, 2.8522, 2.8942, 2.9322, 2.9682, 3.0012,  
                     3.0312, 3.0602, 3.0872, 3.1122, 3.1352, 3.1582, 3.1792, 3.1992, 3.2182, 3.2362],
        "ALFA 0.05":[2.2902, 2.3552, 2.4122, 2.4622, 2.5072, 2.5482, 2.5862, 2.6202, 2.6522, 2.6812, 2.7082,
                     2.7342, 2.7582, 2.7802, 2.8022, 2.8222, 2.8412, 2.8592, 2.8762, 2.8932, 2.9082],
        "ALFA 0.10":[2.1761, 2.2342, 2.2852, 2.3314, 2.3725, 2.4096, 2.4437, 2.4758, 2.5049, 2.531, 2.5571,  
                     2.5801, 2.6031, 2.6241, 2.6441, 2.6631, 2.6811, 2.6981, 2.7141, 2.7291, 2.7431],
    }
)


# Grafica antes

# In[76]:


# Obtener los valores de la columna "Resultado"
resultados = data_sorted["Resultado"]

# Calcular la media y la desviación estándar
media = resultados.mean()
desviacion_estandar = resultados.std()
cv = 

# Crear un rango de valores para la gráfica
x = np.linspace(resultados.min(), resultados.max(), 1000)

# Calcular los valores de la función de densidad de probabilidad (PDF) de la distribución normal
pdf = (1 / (desviacion_estandar * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media) / desviacion_estandar) ** 2)

# Crear la gráfica de densidad
plt.figure(figsize=(8, 6))
sns.lineplot(x=x, y=pdf, color='b', label='Distribución Normal')
plt.title('Distribución Normal de los Resultados')
plt.xlabel('Resultado')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()


# Test de Grubbs manual Mau

# In[116]:


tabla_grubbs = pd.DataFrame(
    {
        "N":[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 
        "ALFA 0.01":[2.4822, 2.5642, 2.6362, 2.6992, 2.7552, 2.8062, 2.8522, 2.8942, 2.9322, 2.9682, 3.0012,  
                     3.0312, 3.0602, 3.0872, 3.1122, 3.1352, 3.1582, 3.1792, 3.1992, 3.2182, 3.2362],
        "ALFA 0.05":[2.2902, 2.3552, 2.4122, 2.4622, 2.5072, 2.5482, 2.5862, 2.6202, 2.6522, 2.6812, 2.7082,
                     2.7342, 2.7582, 2.7802, 2.8022, 2.8222, 2.8412, 2.8592, 2.8762, 2.8932, 2.9082],
        "ALFA 0.10":[2.1761, 2.2342, 2.2852, 2.3314, 2.3725, 2.4096, 2.4437, 2.4758, 2.5049, 2.531, 2.5571,  
                     2.5801, 2.6031, 2.6241, 2.6441, 2.6631, 2.6811, 2.6981, 2.7141, 2.7291, 2.7431],
    }
)

# Datos para buscar

alfa_option = int(input("Ingrese 1 para ALFA 0.10, 2 para ALFA 0.05, o 3 para ALFA 0.01: "))

# Verificar la opción de alfa seleccionada
if alfa_option == 1:
    alfa_column = 'ALFA 0.10'
elif alfa_option == 2:
    alfa_column = 'ALFA 0.05'
elif alfa_option == 3:
    alfa_column = 'ALFA 0.01'
else:
    print("Opción de alfa no válida")
    exit()

n = len(data_sorted)
# Buscar el valor correspondiente en la columna seleccionada
factor_grubbs = tabla_grubbs.loc[tabla_grubbs['N'] == n, alfa_column].values[0]

print(f"Para n = {n} y alfa = {alfa_column}, el valor es: {factor_grubbs}")


# Calculo de limite superior en inferior Test de Grubbs

# In[123]:


limite_superior = media + factor_grubbs * ds
limite_inferior = media - factor_grubbs * ds

# Redondear y luego imprimir los límites
print(round(limite_superior, 2))
print(round(limite_inferior, 2))


# In[ ]:


# Obtener los valores en los índices específicos
menor_atipico = resultados.iloc[0]
mayor_atipico = resultados.iloc[-1]

menor_atipico1 = 0
mayor_atipico1 = 0

# Menor atípico 
if menor_atipico > limite_inferior:
    menor_atipico1 = 1
    print(menor_atipico, "Dato atípico")
else:
    print(menor_atipico, "Dato no atípico")

# Mayor atípico
if mayor_atipico > limite_superior:
    mayor_atipico1 = 1
    print(mayor_atipico, "Dato atípico")
else:
    print(mayor_atipico, "Dato no atípico")

if menor_atipico1 == 1:
    data_sorted = data_sorted.drop(data_sorted.index[0])
    print("Eliminado", menor_atipico1)

if mayor_atipico1 == 1:
    data_sorted = data_sorted.drop(data_sorted.index[-1])
    print("Eliminado", mayor_atipico1)

if menor_atipico1 == 0 and mayor_atipico1 == 0:
    break







# Grubbs

# In[ ]:


while True:

  # Obtener valores min y max
  min_valor = data_sorted["Resultado"].iloc[0] 
  max_valor = data_sorted["Resultado"].iloc[-1]

  # Detectar outliers
  if min_valor < lim_inf:
    outliers.append(min_valor)
    print(f"Valor aberrante: {min_valor}")  

  if max_valor > lim_sup:
    outliers.append(max_valor)
    print(f"Valor aberrante: {max_valor}")
  
  # Eliminar outliers del dataframe
  data_sorted = data_sorted[~(data_sorted < lim_inf) & ~(data_sorted > lim_sup)]  

  # Actualizar n
  n = len(data_sorted)

  # Recalcular estadísticos
  media = data_sorted["Resultado"].mean()
  desv_std = data_sorted["Resultado"].std()

  # Obtener nuevo valor crítico de Grubbs
  factor_grubbs = tabla_grubbs.loc[n, f"ALFA {alfa}"]
  
  # Recalcular límites
  lim_inf = media - factor_grubbs*desv_std
  lim_sup = media + factor_grubbs*desv_std

  if not outliers: 
    break

print("Valores aberrantes eliminados:", outliers)
print("N final:", n)
print("Media final:", media)
print("Desviación estándar final:", desv_std)


# In[ ]:


# Pedir alfa al usuario 
alfa = float(input("Ingrese nivel de significancia (ej: 0.05): "))

# Calcular estadísticos iniciales
n = len(data_sorted)

media = data_sorted["Resultado"].mean()  
desv_std = data_sorted["Resultado"].std()

# Obtener valor crítico de Grubbs
factor_grubbs = tabla_grubbs.loc[n, f"ALFA {alfa}"]

# Calcular límites iniciales
lim_inf = media - factor_grubbs*desv_std
lim_sup = media + factor_grubbs*desv_std
outliers = []

while True:
    condicion = (data_sorted["Resultado"] < lim_inf) | (data_sorted["Resultado"] > lim_sup)
    nuevos_outliers = data_sorted[condicion]

    if len(nuevos_outliers) == 0:
        break

    outliers.extend(nuevos_outliers)
    data_sorted = data_sorted[~condicion]
    
    # Recalcular N
    n = len(data_sorted)
    
    # Recalcular estadísticos
    media = data_sorted["Resultado"].mean()
    desv_std = data_sorted["Resultado"].std()
    cv = (desv_std / media) * 100
    
    # Obtener nuevo valor crítico de Grubbs
    if n < 10:
        factor_grubbs = tabla_grubbs[columna].iloc[0]
    else:
        factor_grubbs = tabla_grubbs[columna].iloc[n - 10]

    # Recalcular límites
    lim_inf = media - factor_grubbs * desv_std
    lim_sup = media + factor_grubbs * desv_std

print(f"Outliers detectados: {outliers}")
print(f"Nueva media: {media}")
print(f"Nueva desviación estándar: {desv_std}")
print(f"Nuevo CV: {cv:.2f}%")
print(f"Nuevos límites: {lim_inf} - {lim_sup}")
print(f"N después de eliminar valores atípicos: {n}")


# Filtro de Dixon Mau

# In[28]:


while True:
    # Obtener los valores de la columna "Resultado"
    resultados = data_sorted["Resultado"]

    # Obtener los valores en los índices específicos
    X1 = resultados.iloc[0]
    X2 = resultados.iloc[1]
    Xn = resultados.iloc[-1]
    Xn1 = resultados.iloc[-2]

    # Calcular los rangos
    rango_dixon = (Xn - X1) / 3
    rango_menor = X2 - X1
    rango_mayor = Xn - Xn1

    X1a = 0
    Xna = 0

    # Menor aberrante 
    if rango_menor > rango_dixon:
        X1a = 1
        print(X1, "Menor Aberrante")
    else: 
        print(X1, "No Aberrante")

    # Mayor aberrante
    if rango_mayor > rango_dixon:
        Xna = 1
        print(Xn, "Mayor Aberrante")
    else: 
        print(Xn, "No Aberrante")

    if X1a == 1:
        data_sorted = data_sorted.drop(data_sorted.index[0])
        print("Eliminado" ,X1)

    if Xna == 1:
        data_sorted = data_sorted.drop(data_sorted.index[-1])
        print("Eliminado ", Xn)

    if X1a == 0 and Xna == 0:
        break


# Grafica Despues

# In[29]:


# Suponiendo que tienes un DataFrame llamado "data_sorted"
# data_sorted = ...

# Obtener los valores de la columna "Resultado"
resultados = data_sorted["Resultado"]

# Calcular la media y la desviación estándar
media = resultados.mean()
desviacion_estandar = resultados.std()

# Crear un rango de valores para la gráfica
x = np.linspace(resultados.min(), resultados.max(), 1000)

# Calcular los valores de la función de densidad de probabilidad (PDF) de la distribución normal
pdf = (1 / (desviacion_estandar * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media) / desviacion_estandar) ** 2)

# Crear la gráfica de densidad
plt.figure(figsize=(8, 6))
sns.lineplot(x=x, y=pdf, color='b', label='Distribución Normal')
plt.title('Distribución Normal de los Resultados')
plt.xlabel('Resultado')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()


# In[129]:


jupyter nbconvert --to python maubox.ipynb

