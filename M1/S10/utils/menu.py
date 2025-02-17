from utils import actions
from utils import data

students_data = []

def menu_student_grade_control():
    option = 0
    while option != 7:
        actions.output_in_CLI("""------------------------------------
- Welcome to student grade control -
------------------------------------
--------- Chose a option -----------
1. Enter information of students
2. See all students' information
3. See best 3 students' average
4. See student's average
5. Export students' information
6. Import students' information
7. Exit program
------------------------------------""")
        option = input_menu()
        direct_actions(option)


def input_menu():
    try:
        option = int(input("Enter an option\n"))
        if option > 7 or option < 1:
            raise IndexError
        else:
            return option
        
    except IndexError:
        actions.output_in_CLI("Error, the option must be between 1 and 7")
    except ValueError as error:
        print(f"Error, value not valid: {error}")


def direct_actions(option):
    global students_data
    if option == 1:
        students_data.append(actions.input_students_data())
    elif option == 2:
        actions.see_all_students_data(students_data)
    elif option == 3:
        actions.see_best_three_students_average(students_data)
    elif option == 4:
        actions.see_each_student_average(students_data)
    elif option == 5:
        data.export_students('students_data.csv',students_data, students_data[0].keys())
    elif option == 6:
        students_data = data.import_students('students_data.csv')
    else:
        actions.output_in_CLI("Thanks for using Student Grade Control")
