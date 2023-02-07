import os
import glob
from csv_utility import Log
from tdr import Csv_tdr

# Define the path where the log files are located
logs_path = "data\Results"

def main():
    # Busca los archivos del directorio
    for path_file in glob.iglob(f'{logs_path}/**', recursive = True):
        # Checa si es un archivo y que no sea GRR    
        if os.path.isfile(path_file) and "GRR" not in path_file and ".csv" in path_file:
            log = Log(path_file)
            log.modify_csv()
            cvs_df = Csv_tdr(path_file)
            

if __name__ == "__main__":
    main()