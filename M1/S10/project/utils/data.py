import csv  # Import the CSV module for reading and writing CSV files

# Function to export student data to a CSV file
def export_students(path, students_data, headers):

    try:
        # Open the file in write mode with UTF-8 encoding and no extra newlines
        with open(path, 'w', encoding='utf-8', newline="") as file:
            # Create a CSV DictWriter object to write dictionaries to the file
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()  # Write the header row to the file
            writer.writerows(students_data)  # Write all student data rows
            print("Data exported correctly")  # Confirm successful export
    except Exception as error:
        # Handle any unexpected errors during file writing
        print(f"Error writing the file: {error}")


# Function to import student data from a CSV file
def import_students(path):
    try:
        # Open the file in read mode
        with open(path, 'r') as file:
            # Use csv.DictReader to read the file into a list of dictionaries
            students_data = list(csv.DictReader(file))
            print("Data imported correctly")  # Confirm successful import
            return students_data  # Return the imported data
    except FileNotFoundError as error:
        # Handle the case where the file does not exist
        print(f"Error, file not found: {error}")
    except IOError as error:
        # Handle other I/O errors (e.g., permission issues, corrupted file)
        print(f"Unexpected error occurred while loading file: {error}")