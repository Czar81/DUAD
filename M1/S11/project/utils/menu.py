# Import necessary modules
from utils import actions  # Contains functions to handle program logic
from utils import data    # Contains functions to import/export data

# Global variable to store student data
students_data = []

# Main function to display the menu and manage user options
def menu_student_grade_control():
    option = 0  # Variable to store the user's selected option
    while option != 7:  # Repeat until the user chooses to exit (option 7)
        # Display the main menu
        print("""------------------------------------
- Welcome to student grade control -
------------------------------------
--------- Choose an option -----------
1. Enter information of students
2. See all students' information
3. See best 3 students' average
4. See student's average
5. Export students' information
6. Import students' information
7. Exit program
------------------------------------""")
        
        # Ask the user to select an option
        option = input_menu()
        
        # Execute the action corresponding to the selected option
        direct_actions(option)


# Function to prompt and validate the menu option
def input_menu():
    try:
        # Ask the user to enter an option
        option = int(input("Enter an option\n"))
        
        # Validate that the option is within the allowed range (1-7)
        if option > 7 or option < 1:
            raise IndexError  # Raise an error if the option is invalid
        else:
            return option  # Return the valid option
        
    except IndexError:
        # Show an error message if the option is not correct
        print("Error, the option must be between 1 and 7")


# Function to execute the action corresponding to the selected option
def direct_actions(option):
    global students_data  # Access the global variable students_data
    if option == 1:
        # Add new student data to the existing list
        students_data += (actions.input_students_data())
    elif option == 2:
        # Display all students' information
        actions.see_all_students_data(students_data)
    elif option == 3:
        # Display the top 3 students by average grade
        actions.see_best_three_students_average(students_data)
    elif option == 4:
        # Display the average grade of each student
        actions.see_each_student_average(students_data)
    elif option == 5:
        # Export student data to a CSV file
        # Check if there is no data to export
        if not students_data:
            print("""------------------------------------
No data to export
------------------------------------""")
            return  # Exit the function if there is no data
        data.export_students('students_data.csv', students_data)
    elif option == 6:
        # Import student data from a CSV file
        students_data += data.import_students('students_data.csv')
    elif option == 7:
        # Exit the program
        print("""------------------------------------
Thanks for using Student Grade Control
------------------------------------""")