import os
import glob
from csv_utility import Log
from tdr import TdrCsv

# Define the path where the log files are located
logs_path = "data\Results"

def main():
    previus_df = None
    # Searh files in directory
    for path_file in glob.iglob(f'{logs_path}/**', recursive = True):
            
        if os.path.isfile(path_file) and "GRR" not in path_file and ".csv" in path_file:
            # print(path_file)
            # log = Log(path_file)
            # reply_modify = log.modify_csv()
            # print(reply_modify)
            dataframe = TdrCsv(path_file, previus_df)
            reply_df = dataframe.set_tempdataframe()
            # print(reply_df)
            previus_df = dataframe.df_main
            status = dataframe.Status
            measurement = dataframe.Measurement
            serial = dataframe.SerialNumber
            if status == "Failed" and measurement == "Passed":
                print(serial)
                print(path_file)

    # create csv
    reply_csv = dataframe.create_csv()
    print(reply_csv)

if __name__ == "__main__":
    main()
