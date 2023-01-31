""" 
The Module 'tdr' short for 'Test Data Record' provides the needed utilities to handle recorded test results
from the generated csv file.
"""

import pandas as pd

path = "data/sample/test.csv"

# Leer archivo original en un dataframe de pandas
df1 = pd.read_csv( path, nrows=3, header= 0)
df1 = df1.iloc[:, 5:]