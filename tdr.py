""" 
The Module 'tdr' short for 'Test Data Record' provides the needed utilities to handle recorded test results
from the generated csv file.
"""

import pandas as pd
import numpy as np

path = "data/sample/test.csv"

# Leer el primer dataframe
df1 = pd.read_csv( path, nrows=3, header= 0)
df1 = df1.iloc[:, 5:]

# Leer el segundo dataframe
df2 = pd.read_csv( path, header= 4)
df2 = df2[['SN', 'Date', 'CycleTime', 'Status', 'FirstFail']]

# Eliminar s de valores"
df2['CycleTime'] = df2['CycleTime'].str.replace('s', '')

# Añadir una columna "Measurement" al segundo dataframe
df2['Measurement'] = 0.0
