""" 
The Module 'csv_utility' modifies the headers of the csv files to be able to insert them in the dataframes.
"""

import csv

class Log:
    def __init__(self, path) -> None:
        """
        Initialize a Log object with the path to the log file.
        """
        self.path = path

    def modify_csv(self):
        """
        Modify the csv file by finding the row with the word "SN" in the 4th or 5th row
        and appending the name of the tests in the row to the dataframe.
        """
        try:
            # Open the csv file for reading
            with open(self.path, 'r') as logfile:
                reader = csv.reader(logfile)
                # Read all the rows into a list
                rows = [row for row in reader]
                csv_header1 = rows[0][6:]

                # Search for the row with the word "SN" in row 4 or 5
                for i, row in enumerate(rows):
                    if i in [3, 4] and "SN" in row:
                        # Copy the name of the tests in the row to the dataframe
                        row += csv_header1
                        break

            # Open the csv file for writing
            with open(self.path, 'w', newline='') as logfile:
                writer = csv.writer(logfile)
                # Write all the rows to the csv file
                writer.writerows(rows)
            return "Modify correct"
        except Exception as e:
            return "Error: " + str(e)