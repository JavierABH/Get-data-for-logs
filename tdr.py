""" 
The Module 'tdr' short for 'Test Data Record' provides the needed utilities to handle recorded test results
from the generated csv file.
"""

import pandas as pd
import clr
import configparser

#local modules
config = configparser.ConfigParser()
config.read('config\settings.ini')

newtonsoftjson_path = config["Paths"]["Newtonsoft.Json.Dll"]
wsconnector_path = config["Paths"]["WSConnector.Dll"]

clr.AddReference(newtonsoftjson_path)
clr.AddReference(wsconnector_path)

from WSConnector import Connector

connector = Connector()

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
        self.df_temp["Measurement"] = ""
        self.df_temp["PartNumber"] = ""
        for i, row in self.df_temp.iterrows():
            if row["Status"] == "Failed":
                measurement = row["FirstFail"]
                # search for the measurement in the header
                measurement_column = self.df_temp.columns.get_loc(measurement)
                # write the value of the measurement in the new column "Measurement"
                self.df_temp.at[i, "Measurement"] = self.df_temp.iloc[i, measurement_column]

            serial = row["SN"]
            resp, serial_partnumber = connector.CIMP_PartNumberRef(serial,1, serial_partnumber)
            self.df_temp.at[i, "PartNumber"] = serial_partnumber  

        self.list_SerialNumber = self.df_temp["SN"]
        self.list_Datetime = self.df_temp["Date"]
        self.list_Cycletime = self.df_temp["CycleTime"]
        self.list_Status = self.df_temp["Status"]
        self.list_FirstFail = self.df_temp["FirstFail"]
        self.list_Date = self.list_Datetime.str.split(" ").str[0]
        self.list_Measurement = self.df_temp["Measurement"]
        self.list_PartNumber = self.df_temp["PartNumber"]

    