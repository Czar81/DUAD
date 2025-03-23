import os
from utils.import_csv import import_data_category_csv

def _verify_if_file_exist(path="exports/data.csv"):
    if os.path.exists(path):
        if os.path.getsize(path) > 0:
            return True
        else:
            return False
    else:
        return False


def _verify_movement(new_movement):
    if not _verify_if_category_exist(new_category=new_movement[2]):
        raise ValueError("Category already exists")
    for item in new_movement:
        if item is None:
            raise ValueError("There can not be empty fields")
    if not __verify_if_is_number(new_movement[1]):
        raise ValueError("Amount must be a number")


def _verify_if_category_exist(new_category=None):
    categories = import_data_category_csv()
    for category in categories:
        if category.strip().lower() == new_category.strip().lower():
            return True
    return False



def __verify_if_is_number(value):
    if isinstance(value,(int,float, complex)):
        return True
    return False