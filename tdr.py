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
# Paths to external DLL files
newtonsoftjson_path = config["Paths"]["Newtonsoft.Json.Dll"]
wsconnector_path = config["Paths"]["WSConnector.Dll"]
# Adding references to the external DLL files
clr.AddReference(newtonsoftjson_path)
clr.AddReference(wsconnector_path)
# Importing the Connector class from the WSConnector module
from WSConnector import Connector
# Instance of the Connector class
connector = Connector()

class Tdr:
    def __init__(self, path) -> None:
        # Path to the csv file
        self.path = path
        # DataFrame used to temporarily store the csv data
        self.df_temp = None
        # Initializing the following lists to None
        self.list_SerialNumber = None
        self.list_Datetime = None
        self.list_Date = None
        self.list_Cycletime = None
        self.list_PartNumber = None
        self.list_Status = None
        self.list_FirstFail = None
        self.list_Measurement = None
        # DataFrame used to temporarily store the csv data
        self.df_temp = None
        # Calling the method to set the temporary dataframe
        self.set_tempdataframe()

    # Method to set the temporary dataframe
    def set_tempdataframe(self):
        # Reading the csv file and storing it in the temporary dataframe
        self.df_temp = pd.read_csv(self.path, header=4)
        # Adding empty columns
        self.df_temp["Measurement"] = ""
        self.df_temp["PartNumber"] = ""
        # Iterating through the rows of the dataframe
        for i, row in self.df_temp.iterrows():
            # If the row's "Status" value is "Failed"
            if row["Status"] == "Failed":
                # Getting the value of the "FirstFail" column
                measurement = row["FirstFail"]
                # search for the measurement in the header
                measurement_column = self.df_temp.columns.get_loc(measurement)
                # write the value of the measurement in the new column "Measurement"
                self.df_temp.at[i, "Measurement"] = self.df_temp.iloc[i, measurement_column]
            # Getting the value of the "SN" (Serial Number) column
            serial = row["SN"]
            # If serial is blank, leave partnumber empty
            if serial != "":
                # Getting the part number for the serial number
                resp, serial_partnumber = connector.CIMP_PartNumberRef(serial,1, serial_partnumber)
                # Writing the part number in the "PartNumber" column
                self.df_temp.at[i, "PartNumber"] = serial_partnumber 
        # Store the data from the dataframe into separate lists.
        self.list_SerialNumber = self.df_temp["SN"]
        self.list_Datetime = self.df_temp["Date"]
        self.list_Cycletime = self.df_temp["CycleTime"]
        self.list_Status = self.df_temp["Status"]
        self.list_FirstFail = self.df_temp["FirstFail"]
        self.list_Measurement = self.df_temp["Measurement"]
        self.list_PartNumber = self.df_temp["PartNumber"]
        # Split the date of the time
        self.list_Date = self.list_Datetime.str.split(" ").str[0]