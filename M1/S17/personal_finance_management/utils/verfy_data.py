import os

def _verify_if_data_exist(path):
    if os.path.exists(path):
        if os.path.getsize(path) > 0:
            return True
        else:
            return False
    else:
        return False


def _verify_if_category_exist(path="data/categories.csv"):
    pass