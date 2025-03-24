import csv
from FreeSimpleGUI import popup
from utils.verify_data import _verify_movement, _verify_category


def export_category(path="data/categories.csv", new_category=None):
    """    
    Export a new category to the categories CSV file.
    """
    try:
        # Open the file
        with open(file=path, mode='a',newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Verify category
            _verify_category(new_category)
            # Verify if the file is empty
            if file.tell() == 0:
                # Write headers
                writer.writerow(["Category"])
            # Write row
            writer.writerow([new_category])
            popup("Category has beed added successfully!")
    except ValueError as error:
        popup(error, title="Error in export category")
    except csv.Error as error:
        popup(f"An unexpected error ocurred with csv trying to export category: {error}", title="Error in export category")
    except Exception as error:
        popup(f"An unexpected error ocurred with export_category: {error}", title="Error in export category")

def export_movements(path="exports/data.csv", new_movement=None):
    try:
        # Call a function to verify if the movement is correct
        _verify_movement(new_movement)
        # Open the file
        with open(file=path, mode='a',newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Verify if the file is empty
            if file.tell() == 0:
                # Write headers
                writer.writerow(["Title", "Amount", "Category"])
            # Write row
            writer.writerow(new_movement)
            popup("Movement has been added successfully!")
    except ValueError as error:
        popup(error)
    except FileNotFoundError as error:
        popup(f"Error, trying to create file: {error}", title="Error in export movement")
    except csv.Error as error:
        popup(f"An unexpected error ocurred with csv: {error}", title="Error in export movement")
    except Exception as error:
        popup(f"An unexpected error ocurred with export_movements: {error}", title="Error in export movement")