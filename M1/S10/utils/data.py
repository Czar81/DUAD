import csv

def export_students(path, students_data, headers):
    if not students_data:
        print("No data to export.")
        return
    try:
        with open(path, 'w', encoding = 'utf-8', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students_data)
            print("Data export correctly")
    except Exception as error:
        print(f"Error writing the file: {error}")


def import_students(path):
    try:
        with open(path, 'r') as file:
            students_data = list(csv.DictReader(file))
            print("Data import correctly")
            return students_data
    except FileNotFoundError as error:
        print(f"Error, file not found: {error}")
    except IOError as error:
        print(f"Unexpected error ocurred while loading file: {error}")