""" 
The Module 'tdr' short for 'Test Data Record' provides the needed utilities to handle recorded test results
from the generated csv file.
"""

import pandas as pd

# Leer archivo original en un dataframe de pandas
df = pd.read_csv("data/sample/input.csv", header = 4)