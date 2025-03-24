import csv
import os
from FreeSimpleGUI import popup

def import_data_table_csv(path="exports/data.csv"):
    """ 
    Import transaction data from a CSV file
    """
    data_import = []
    try:
        # Verify is the file exist
        if os.path.exists(path):
            # Open file
            with open(file=path, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                # Skip headers
                next(reader)
                # Iterate on every row
                for row in reader:
                    # Add a row to the list data_import
                    data_import.append(row)
            return data_import
        else:
            # If the file not exist return empty list
            return []
    # Change and add exception
    except Exception as error:
        popup(f"An unexpected error ocurred trying to read data.csv {error}", title="Error in export import_data_table_csv")
        return []
    except csv.Error as error:
        popup(f"CSV format error: {error}", title="Format error in import_data_table_csv")
        return []
    except PermissionError as error:
        popup("Error: No permissions to read the file", title="Permissions error in import_data_table_csv")
        return []


def import_data_category_csv(path="data/categories.csv"):
    """ 
    Import categories from a CSV file
    """
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
        popup(f"An unexpected error ocurred trying to read categories.csv", title="Error in import_data_category_csv")
        return []
    except csv.Error as error:
        popup(f"CSV format error: {error}", title="Format error in import_data_category_csv")
        return []
    except PermissionError as error:
        popup("Error: No permissions to read the file", title="Permissions error in import_data_category_csv")
        return []