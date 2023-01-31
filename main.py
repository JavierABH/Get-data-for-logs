import csv
import os
import glob
import pandas as pd
import numpy as np

logs_path = "data\Results"

def main():
    for path_file in glob.iglob(f'{logs_path}/**', recursive = True):
        if os.path.isfile(path_file)
            # Abrir el archivo csv para lectura
            with open(path, 'r') as f:
            reader = csv.reader(f)

            # Leer todas las filas en una lista
            rows = [row for row in reader]

            # Modificar la fila 5
            rows[4] = rows[4] + [''] * 150

            # Abrir el archivo csv para escritura
            with open(path, 'w', newline='') as f:
            writer = csv.writer(f)

            # Escribir todas las filas en el archivo csv
            writer.writerows(rows)

if __name__ == "__main__":
    main()