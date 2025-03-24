from utils.import_csv import import_data_category_csv

def _verify_category(new_category=""):
    """
    Validates a new category before adding it to file
    """
    # Verify if new_category is a empty string
    if new_category == "":
        raise ValueError("Category cant not be empty")
    # Call __verify_if_category_exist and if
    elif __verify_if_category_exist(new_category):
        raise ValueError("Category already exists")

def _verify_movement(new_movement=""):
    """
    Validates a new movement before adding it to file
    """
    # Vefiry if the first and last are empty raise ValueError
    if new_movement[0] == "" or new_movement[1] == "":
        raise ValueError("There can not be empty fields")
    # Vefiry if the combo are empty, and raise ValueError
    if new_movement[2] == "":
        raise ValueError("Select one category or make it first")
    # Call a function to vefiry if the Amount is a nunmber
    if not __verify_if_is_number(new_movement[1]):
        raise ValueError("Amount must be a number")


def __verify_if_category_exist(new_category=None):
    """
    Verify if the category already exist in the file
    """

    # Call import_data_category_csv to compare data
    categories = import_data_category_csv()
    # Eliminate blank space and convert to lower
    category = category.strip().lower()
    # Iterate the list of categories
    for category in categories:
        # Look if the category exist
        if  category == new_category.strip().lower():
            return True
    return False



def __verify_if_is_number(value):
    """
    Verify if a value is a number
    """
    try:
        # Convert the value to float
        value = float(value)
        # Verify if value is a float
        if isinstance(value,(float)):
            return True
        # If not return False
        return False
    except Exception:
        # If it fail on convert string to float return False
        return False