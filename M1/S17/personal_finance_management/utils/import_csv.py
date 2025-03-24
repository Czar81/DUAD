import csv
import os
from FreeSimpleGUI import popup

def import_data_table_csv(path="exports/data.csv"):
    data_import = []
    try:
        if os.path.exists(path):
            with open(file=path, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    data_import.append(row)
            return data_import
        else:
            return []
    # Change and add exception
    except Exception as error:
        popup(f"An unexpected error ocurred trying to read data.csv {error}")


def import_data_category_csv(path="data/categories.csv"):
    try:
        if os.path.exists(path):
            with open(file=path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                categories = [row["Category"] for row in reader]
            return categories
        else:
            return []
    # Change and add exception
    except Exception as error:
        popup(f"An unexpected error ocurred trying to read categories.csv")
