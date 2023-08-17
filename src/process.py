import pandas as pd

class Process:

  # Constructor
  def __init__(self):
        pass

  # Tests de Grubbs
  def grubbs(self, data, media, ds):
        
          # Tabla en la que utilizamos segun el usuario escoja el nivel de confianza opcion 1 0.10 osea 90% de confianza , 
  # opcion 2  0.05 osea 95% de confianza y opcion 3 0.01 osea 99% de confianza,
  # Hay que tener en cuenta que el N comienza de 1o hasta el 30 mas de esos limites no hay calculo  

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

    n = len(data)
    # Buscar el valor correspondiente en la columna seleccionada
    factor_grubbs = tabla_grubbs.loc[tabla_grubbs['N'] == n, alfa_column].values[0]

    # Aqui calculamos los limites superior e inferior de donde partimos para encontrar
    # los valores a tipicos u outliers

    limite_superior = media + factor_grubbs * ds
    limite_inferior = media - factor_grubbs * ds

    # Redondear y luego imprimir los límites

    print('El limite inferior es:', round(limite_inferior, 2))
    print('El limite superior es:', round(limite_superior, 2))

    # Codigo que se basa segun los limites antes calculados para eliminar y rectificar si hay 
    # mas valores atipicos luego de los ciclos los imprime y los elimina tambien debne aparecer en la GUI
    while True:
      menor_atipico = data["Resultado"].iloc[0]
      mayor_atipico = data["Resultado"].iloc[-1]

      # Menor atípico
      if menor_atipico < limite_inferior:
          print(menor_atipico, "es Dato atípico")
          data = data.drop(data.index[0])
          print(menor_atipico, "Eliminado")
          
      else:
          print(menor_atipico, "es Dato no atípico")

      # Mayor atípico
      if mayor_atipico > limite_superior:
          print(mayor_atipico, "es Dato atípico")
          data = data.drop(data.index[-1])
          print(mayor_atipico, "Eliminado")

      else:
          print(mayor_atipico, "es Dato no atípico")

      if menor_atipico >= limite_inferior and mayor_atipico <= limite_superior:
          break
    print(f"Para n = {n} y alfa = {alfa_column}, el valor del factor de Grubbs es: {factor_grubbs}")
    #  Esto se va a imprimir en la interfaz de usuario       
    clean_data = data.copy()
    return(clean_data)
  
     ########################################################################
     ########################################################################
     ########################################################################

    # Filtro Dixon 
  def dixon(self, data):
        # Aplicar filtro de Dixon u otros métodos aquí
    while True:
        # Obtener los valores de la columna "Resultado"
        data = data["Resultado"]

        data = data.reset_index(drop=True)

        # Obtener los valores en los índices específicos
        X1 = data.iloc[0]
        X2 = data.iloc[1]
        Xn = data.iloc[-1]
        Xn1 = data.iloc[-2]

        # Calcular los rangos
        rango_dixon = (Xn - X1) / 3
        rango_menor = X2 - X1
        rango_mayor = Xn - Xn1

      
        # Menor aberrante 
        if rango_menor > rango_dixon:
            data = data.drop(data.index[0])
            print("Eliminado", X1)
            print(X1, "Menor Aberrante")
        else: 
            print(X1, "No Aberrante")

        # Mayor aberrante
        if rango_mayor > rango_dixon:
            data = data.drop(data.index[-1])
            print("Eliminado", Xn)
            print(Xn, "Mayor Aberrante")
        else: 
            print(Xn, "No Aberrante") 

        if rango_menor <= rango_dixon and rango_mayor <= rango_dixon:
            break

        clean_data = data.copy()

        return(clean_data)
            
             









