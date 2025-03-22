import csv
from utils.verfy_data import _verify_if_data_exist
def import_data_table_csv(path="exports/data.csv"):
    data_import = []
    exist_data = _verify_if_data_exist(path)
    if exist_data:
        with open(file=path, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data_import.append(row)
        return data_import
    else:
        return []


def import_data_category_csv(path="data/categories.csv"):
    categories = []
    exist_data = _verify_if_data_exist(path)
    if exist_data:
        with open(file=path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            categories = [row["Category"] for row in reader]
        return categories
    else:
        return None