# Grafica antes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import data
import seaborn as sn
# In[10]:

# data_sorted1 = data.sort_values(by="Resultado")
# Graficamos antes con una distrubucion normal para saber el estado de los datos y 
# su distribucion Gaussiana
# Obtener los valores de la columna "Resultado"
resultados1 = data_sorted1["Resultado"]

# Crear un rango de valores para la gráfica
x = np.linspace(resultados1.min(), resultados1.max(), 1000)

# Calcular los valores de la función de densidad de probabilidad (PDF) de la distribución normal
pdf = (1 / (ds_antes * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media_antes) / ds_antes) ** 2)

# Crear la gráfica de densidad antes
plt.figure(figsize=(8, 6))
sns.lineplot(x=x, y=pdf, color='b', label='Distribución Normal')
plt.title('Distribución Normal de los resultados antes')
plt.xlabel('Resultado')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()


# Grafica Despues de aplicar los filtros

# In[17]:


# Esta grafica tambien va a aparecer e la GUI al lado derecho de la grafica de distribucion normal
# de antes
# Obtener los valores de la columna "Resultado" de data_sorted2
resultados2 = data_sorted2["Resultado"]

# Crear un rango de valores para la gráfica
x = np.linspace(resultados2.min(), resultados2.max(), 1000)

# Calcular los valores de la función de densidad de probabilidad (PDF) de la distribución normal
pdf = (1 / (ds_despues * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media_despues) / ds_despues) ** 2)

# Crear la gráfica de densidad
plt.figure(figsize=(8, 6))
sns.lineplot(x=x, y=pdf, color='b', label='Distribución Normal')
plt.title('Distribución Normal de los resultados después')
plt.xlabel('Resultado')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()
