from utils.import_csv import import_data_category_csv

def _verify_category(new_category=""):
    if new_category == "":
        raise ValueError("Category cant not be empty")
    elif not __verify_if_category_exist(new_category):
        raise ValueError("Category already exists")

def _verify_movement(new_movement=""):
    if new_movement[0] == "" or new_movement[1] == "":
        raise ValueError("There can not be empty fields")
    if new_movement[2] == "":
        raise ValueError("Select one category or make it first")
    if not __verify_if_is_number(new_movement[1]):
        raise ValueError("Amount must be a number")


def __verify_if_category_exist(new_category=None):
    categories = import_data_category_csv()
    for category in categories:
        if category.strip().lower() == new_category.strip().lower():
            return True
    return False



def __verify_if_is_number(value):
    try:
        value = float(value)
        if isinstance(value,(int,float, complex)):
            return True
        return False
    except Exception:
        return False