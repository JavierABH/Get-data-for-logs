import csv
import os
import glob
import pandas as pd
import numpy as np

path = "data/sample/input.csv"

def main():
    logs_path = "data\Results"
    # Busca los archivos del directorio
    # for path_file in glob.iglob(f'{logs_path}/**', recursive = True):
    #     # Checa si es un archivo y que no sea GRR
    #     if os.path.isfile(path_file) and "GRR" not in path_file:
    #        change_csv(path_file)

def change_csv(path_file):
    # Abrir el archivo csv para lectura
            with open(path_file, 'r') as logfile:
                reader = csv.reader(logfile)
                # Leer todas las filas en una lista
                rows = [row for row in reader]
                csv_header1 = rows[0][6:]

            # Buscar la fila con la palabra "SN" en la fila 4 o 5
                for i, row in enumerate(rows):
                    if i in [3, 4] and "SN" in row:
                        # Copia el nombre de las pruebas en la fila para el dataframe
                        row += csv_header1
                        break

            # Abrir el archivo csv para escritura
            with open(path_file, 'w', newline='') as logfile:
                writer = csv.writer(logfile)
                # Escribir todas las filas en el archivo csv
                writer.writerows(rows)
                print(path_file)

if __name__ == "__main__":
    main()