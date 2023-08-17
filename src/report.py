import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Plots:
    
    def grafica_antes(data, ds, media):
    # Grafica pa antes de aplicar filtro

        # Graficamos antes con una distrubucion normal para saber el estado de los datos y 
        # su distribucion Gaussiana
        # Obtener los valores de la columna "Resultado"
        Resultados = data["Resultados"]

        # Crear un rango de valores para la gráfica
        x = np.linspace(Resultados.min(), Resultados.max(), 1000)

        # Calcular los valores de la función de densidad de probabilidad (PDF) de la distribución normal
        pdf = (1 / (ds * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media) / ds) ** 2)

        # Crear la gráfica de densidad antes
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=x, y=pdf, color='b', label='Distribución Normal')
        plt.title('Distribución Normal de los resultados antes')
        plt.xlabel('Resultado')
        plt.ylabel('Densidad de Probabilidad')
        plt.legend()
        plt.grid(True)
        plt.show()

    ###################################################################################
    ###################################################################################

    #Grafica despues de aplicado los filtros

    def grafica_despues(data, ds_despues, media_despues):
    # Grafica pa antes de aplicar filtro

        # Graficamos antes con una distrubucion normal para saber el estado de los datos y 
        # su distribucion Gaussiana
        # Obtener los valores de la columna "Resultado"
        Resultados = data["Resultados"]

        # Crear un rango de valores para la gráfica
        x = np.linspace(Resultados.min(), Resultados.max(), 1000)

        # Calcular los valores de la función de densidad de probabilidad (PDF) de la distribución normal
        pdf = (1 / (ds_despues * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media_despues) / ds_despues) ** 2)

        # Crear la gráfica de densidad antes
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=x, y=pdf, color='b', label='Distribución Normal')
        plt.title('Distribución Normal de los resultados antes')
        plt.xlabel('Resultado')
        plt.ylabel('Densidad de Probabilidad')
        plt.legend()
        plt.grid(True)
        plt.show()

# Nota importante como se usa la clase con una instancia 
# plots = Plots()
# plots.grafica_antes(data, ds, media) ###Parahacer la garfica antes
# La instancia es plots = Plots()
# y para graficar seria plots.grafica_antes(data, ds, media)
