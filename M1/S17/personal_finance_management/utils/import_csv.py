import csv
import os
def _import_data_table_csv(path):
    data_import = []
    exist_data = __verify_if_data_exist(path)
    if exist_data:
        with open(path, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data_import.append(row)
        return data_import
    else:
        return []


def _import_data_category_csv(path="C:/Users/Aaron/VS/Lyfther/DUAD/M1/S17/personal_finance_management/exports/data.csv"):
    categories = []
    exist_data = __verify_if_data_exist(path)
    if exist_data:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            categories = [row["Category"] for row in reader]
        categories_clean=__remove_duplicates(categories)
        return categories_clean
    else:
        return []

def __verify_if_data_exist(path):
    if os.path.exists(path):
        if os.path.getsize(path) > 0:
            return True
        else:
            return False
    else:
        return False


def __remove_duplicates(categories):
    return list(set(categories))