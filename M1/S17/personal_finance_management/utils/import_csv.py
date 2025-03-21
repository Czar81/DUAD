import csv
import os
def _import_data_csv(path):
    data_import = []
    #exist_data = __verify_if_data_exist(path)
    #if exist_data == True:
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data_import.append(row)
    print(data_import)
    return data_import
    #else:
     #   return []


def __verify_if_data_exist(path):
    if os.path.exists(path):
        if os.path.getsize(path) > 0:
            return True
        else:
            return False
    else:
        return False