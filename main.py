import csv
import glob
import pandas as pd
import numpy as np

logs_path = "data\Results"
path = "data/sample/test.csv"

def main():
    for path in glob.iglob(f'{logs_path}/*'):
        print(path)




    # # Leer el primer dataframe
    # df1 = pd.read_csv( path, nrows=3, header= 0)
    # df1 = df1.iloc[:, 5:]

    # # Leer el segundo dataframe
    # df2 = pd.read_csv( path, header= 4)
    # df2 = df2[['SN', 'Date', 'CycleTime', 'Status', 'FirstFail']]

    # # Eliminar s de valores"
    # df2['CycleTime'] = df2['CycleTime'].str.replace('s', '')

    # # Añadir una columna "Measurement" al segundo dataframe
    # df2['Measurement'] = 0.0



if __name__ == "__main__":
    main()