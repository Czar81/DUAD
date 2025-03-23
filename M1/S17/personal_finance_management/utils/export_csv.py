import csv
from FreeSimpleGUI import popup
from utils.verfy_data import _verify_movement, _verify_if_category_exist


def export_category(path="data/categories.csv", new_category=None):
    try:
        if _verify_if_category_exist:
            raise ValueError
        with open(file=path, mode='a',newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Category"])
            writer.writerow([new_category])
    except ValueError:
        popup("Category already exists")
    except csv.Error as error:
        popup(f"An unexpected error ocurred with csv trying to export category: {error}")
    except Exception as error:
        popup(f"An unexpected error ocurred with export_category: {error}")

def export_movements(path="exports/data.csv", new_movement=None):
    try:
        _verify_movement(new_movement)
        with open(file=path, mode='a',newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Title", "Amount", "Category"])
            writer.writerow(new_movement)
    except ValueError as error:
        popup(error)
    except FileNotFoundError as error:
        popup(f"Error, trying to create file: {error}")
    except csv.Error as error:
        popup(f"An unexpected error ocurred with csv: {error}")
    except Exception as error:
        popup(f"An unexpected error ocurred with export_movements: {error}")