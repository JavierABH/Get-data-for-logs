""" 
The Module 'tdr' short for 'Test Data Record' provides the needed utilities to handle recorded test results
from the generated csv file.
"""

import pandas as pd

class Csv_tdr:
    def __init__(self, path) -> None:
        self.path = path
        self.df_temp = None
        self.list_SerialNumber = None
        self.list_Datetime = None
        self.list_Date = None
        self.list_Cycletime = None
        self.list_PartNumber = None
        self.list_Status = None
        self.list_FirstFail = None
        self.list_Measurement = None
        self.df_temp = None
        self.set_tempdataframe()

    def set_tempdataframe(self):
        self.df_temp = pd.read_csv(self.path, header=4)
        self.list_SerialNumber = self.df_temp["SN"]
        self.list_Datetime = self.df_temp["Date"]
        self.list_Cycletime = self.df_temp["CycleTime"]
        self.list_Status = self.df_temp["Status"]
        self.list_FirstFail = self.df_temp["FirstFail"]
        self.list_Date = self.list_Datetime.str.split(" ").str[0]
        self.df_temp["Measurement"] = float("NaN")
        for i, row in self.df_temp.iterrows():
            if row["Status"] == "Failed":
                measurement = row["FirstFail"]
                # search for the measurement in the header
                measurement_column = self.df_temp.columns.get_loc(measurement)
                # write the value of the measurement in the new column "Measurement"
                self.df_temp.at[i, "Measurement"] = self.df_temp.iloc[i, measurement_column]
        self.list_Measurement = self.df_temp["Measurement"]

    