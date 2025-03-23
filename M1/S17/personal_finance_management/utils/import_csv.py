import csv
import os

def import_data_table_csv(path="exports/data.csv"):
    data_import = []

    if os.path.exists(path):
        with open(file=path, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data_import.append(row)
        return data_import
    else:
        return None


def import_data_category_csv(path="data/categories.csv"):
    if os.path.exists(path):
        with open(file=path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            categories = [row["Category"] for row in reader]
        return categories
    else:
        return []