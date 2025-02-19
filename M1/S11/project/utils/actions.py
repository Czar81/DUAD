from utils import student # Import Student class with the necessary attributes

# Function to input student data
def input_students_data():
    students_data = []  # List to store all student data
    amount_students = input_number_students()  # Get the number of students
    for i in range(amount_students):  # Loop through each student
        # Input student name
        name = input(f"Enter the student name {i+1}\n")
        # Input student section
        section = input(f"Enter the student section {i+1}\n")
        # Input Spanish note
        spanish_note = input_student_note("spanish")
        # Input English note
        english_note = input_student_note("english")
        # Input Social Studies note
        social_studies_note = input_student_note("social studies")
        # Input Science note
        science_note = input_student_note("science")
        # Add the student's data to the list
        students_data.append(student.StudentClass(name, section, spanish_note, english_note, social_studies_note, science_note))
    return students_data  # Return the list of student data


# Function to display all students' data
def see_all_students_data(students_data):
    # Display header for all students' data
    print("""------------------------------------
-------- All Students Data ---------
------------------------------------""")
    # Loop through each student and display their data
    for student in students_data:
        print(f"""NAME: {student.name}
SECTION: {student.section}
SPANISH NOTE: {student.spanish_note}
ENGLISH NOTE: {student.english_note}
SOCIAL STUDIES NOTE: {student.english_note}
SCIENCE NOTE: {student.science_note}
------------------------------------""")


# Function to display the top 3 students by average grade
def see_best_three_students_average(students_data):
    averages = []  # List to store student averages
    # Calculate the average grade for each student
    for student in students_data:
        average = (int(student.spanish_note) + int(student.english_note)
                + int(student.social_studies_note) + int(student.science_note)) / 4
        # Store the student's name and average
        averages.append({'name': student.name, 'average': average})
    # Sort the averages in descending order
    averages.sort(key=lambda x: x['average'], reverse=True)
    # Display header for top 3 averages
    print("""------------------------------------
--------- Best 3 averages ----------
------------------------------------""")
    # Display the top 3 students
    for i in range(min(3, len(averages))):  # Ensure there are at least 3 students
        print(f"""-- TOP {i+1} ---------------------------
NAME: {averages[i]['name']}
AVERAGE: {averages[i]['average']}) 
------------------------------------""")


# Function to display the average grade of each student
def see_each_student_average(students_data):
    # Display header for students' averages
    print("""------------------------------------
-------- Students Averages ---------
------------------------------------""")
    # Calculate and display the average for each student
    for student in students_data:
        average = (int(student.spanish_note) + int(student.english_note)
                + int(student.social_studies_note) + int(student.science_note)) / 4
        print(f"NAME: {student.name} \nAVERAGE: {average}\n------------------------------------")


# Function to input the number of students
def input_number_students():
    while True:
        try:
            # Ask the user to enter the number of students
            amount_students = int(input("Enter the number of students\n"))
            if amount_students < 0:  # Validate that the number is positive
                raise ValueError
            else:
                return amount_students  # Return the valid number
        except ValueError as error:
            # Display error if the input is not a valid number
            print(f"Error, invalid value must be a positive number: {error}")


# Function to input a student's note for a subject
def input_student_note(subject):
    while True:
        try:
            # Ask the user to enter the note for the subject
            note = int(input(f"Enter the note of {subject}\n"))
            if note > 100 or note < 1:  # Validate that the note is between 1 and 100
                raise ValueError
            else:
                return note  # Return the valid note
        except ValueError:
            # Display error if the input is not a valid numberd
            print(f"Error, the note must be between 1 and 100")