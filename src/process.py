# Procesar datos
def process_data(data):

  clean_data = filter_outliers(data)
  
  results = create_results(clean_data)

  return results


# Filtrar outliers 
def filter_outliers(data):
  
  sorted_data = sort_data(data)
  
# aplicar filtro de dixon 
  
  return filtered_data


# Crear dataframe de resultados
def create_results(clean_data):

  results = pd.DataFrame()
  results["Fecha"] = clean_data.index
  results["Dato"] = clean_data["Dato"]  

  return results

