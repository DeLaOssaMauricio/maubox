# utils.py
import pandas as pd

def read_excel(file):
  return pd.read_excel(file)

def read_excel(file):
  """
  Lee un archivo Excel y retorna un DataFrame.

  Examples:
  >>> df = read_excel('data.xlsx')
  >>> print(df.shape)
  (100, 3)
  """

  return pd.read_excel(file)