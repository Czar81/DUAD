import csv  # Import the CSV module for reading and writing CSV files
from utils import student # Import Student class with the necessary attributes

# Function to export student data to a CSV file
def export_students(path, students_data):
    headers = (
        "name",
        "section",
        "spanish_note",
        "english_note",
        "social_studies_note",
        "science_note"
    )
    
    try:
        # Open the file in write mode with UTF-8 encoding and no extra newlines
        with open(path, 'w', encoding='utf-8', newline="") as file:
            # Create a CSV DictWriter object to write dictionaries to the file
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()  # Write the header row to the file
            # Write all student data rows
            for student in students_data:
                writer.writerow({
                    "name": student.name,
                    "section": student.section,
                    "spanish_note": student.spanish_note,
                    "english_note": student.english_note,
                    "social_studies_note": student.social_studies_note,
                    "science_note": student.science_note
                })  
            print("Data exported correctly")  # Confirm successful export
    except Exception as error:
        # Handle any unexpected errors during file writing
        print(f"Error writing the file: {error}")


# Function to import student data from a CSV file
def import_students(path):
    students = []
    try:
        # Open the file in read mode
        with open(path, 'r') as file:
            # Use csv.DictReader to read the file into a list of dictionaries
            students_data = list(csv.DictReader(file))
            # Convert each student and its own data to Object and then to list of Objets
            for row in students_data:
                # Instance of Student with its attributes
                student_data = student.StudentClass(name=row['name'], section=row['section'], spanish_note=row['spanish_note'], english_note=row['english_note'],
                                     social_studies_note=row['social_studies_note'], science_note=row['science_note'])
                # Add the object to the list students
                students.append(student_data)
            print("Data imported correctly")  # Confirm successful import
            return students  # Return the imported data
    except FileNotFoundError as error:
        # Handle the case where the file does not exist
        print(f"Error, file not found: {error}")
    except IOError as error:
        # Handle other I/O errors (e.g., permission issues, corrupted file)
        print(f"Unexpected error occurred while loading file: {error}")