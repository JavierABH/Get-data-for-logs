import csv
import os
import glob
import pandas as pd
import numpy as np
from csv_utility import Log

# Define the path where the log files are located
logs_path = "data\Results"

def main():
    # Busca los archivos del directorio
    for path_file in glob.iglob(f'{logs_path}/**', recursive = True):
        # Checa si es un archivo y que no sea GRR    
        if os.path.isfile(path_file) and "GRR" not in path_file:
            log = Log(path_file)
            log.modify_csv()


if __name__ == "__main__":
    main()