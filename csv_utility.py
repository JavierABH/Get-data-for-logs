import csv
class Csv: 
    def __init__(self, path) -> None:
        """
        Initialize a Csv object with the path to the logfiles.
        """
        self.path = path
    
    # Obtener las lineas del archivo csv para lectura
    def get_lines(self):
        with open(self.path, 'r') as logfile:
            reader = csv.reader(logfile)
            # Leer todas las filas en una lista
            rows = [row for row in reader]
            return rows

    def change_line(rows):
        target_row = 'SN,Date,Rack,Nest,Status,FirstFail'
        num_commas = 150
        for i, row in enumerate(rows):
            if row == [target_row]:
                rows[i] = row + [''] * num_commas
                break
    