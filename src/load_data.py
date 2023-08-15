# load_data.py

import pandas as pd
from tkinter import filedialog

def get_file():
   file_path = filedialog.askopenfilename()
   return file_path

def load_data(file_path):
   try:
      df = pd.read_excel(file_path)
   except Exception as e:   
      raise ValueError(f"Error leyendo archivo: {e}")

   validate_columns(df)
   
   return df

def validate_columns(df):
   columns_required = ["Fecha", "Dato"]
   
   missing_cols = set(columns_required) - set(df.columns)
   if missing_cols:
      raise ValueError(f"Columnas faltantes: {missing_cols}")