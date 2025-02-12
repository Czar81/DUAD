def input_students_data():
    students_data = []
    amount_students = input_number_students()
    for i in range(amount_students):
        student_data = {}
        #name
        student_data['name'] = input(f"Enter the student name {i+1}\n")
        #section
        student_data['section'] = input(f"Enter the student section {i+1}\n")
        #note spanish
        student_data['spanish_note'] = input_student_note("spanish")
        #note english
        student_data['english_note'] = input_student_note("english")
        #note social studies
        student_data['social_studies_note'] = input_student_note("social studies")
        #note science
        student_data['science_note'] = input_student_note("science")
        students_data.append(student_data)
    return students_data


def see_all_students_data(students_data):
    output_in_CLI("""------------------------------------
-------- All Students Data ---------
------------------------------------""")
    for student in students_data:
        print(f"""NAME: {student['name']}
SECTION: {student['section']}
SPANISH NOTE: {student['spanish_note']}
ENGLISH NOTE: {student['english_note']}
SOCIAL STUDIES NOTE: {student['social_studies_note']}
SCIENCE NOTE: {student['science_note']}
------------------------------------""")


def see_best_three_students_average(students_data):
    averages = []
    for student in students_data:
        average = (int(student['spanish_note']) + int(student['english_note'])
                + int(student['social_studies_note']) + int(student['science_note'])) / 4
        averages.append({'name': student['name'], 'average': average})
    averages.sort(key=lambda x: x['average'], reverse=True)
    output_in_CLI("""------------------------------------
--------- Best 3 averages ----------
------------------------------------""")
    for i in range(min(3, len(averages))):
        print(f"""-- TOP {i+1} ---------------------------
NAME: {averages[i]['name']}
AVERAGE: {averages[i]['average']}") 
------------------------------------""")


def see_each_student_average(students_data):
    output_in_CLI("""------------------------------------
-------- Students Averages ---------
------------------------------------""")
    for student in students_data:
        average = (int(student['spanish_note']) + int(student['english_note'])
                + int(student['social_studies_note']) + int(student['science_note'])) / 4
        print(f"NAME: {student['name']} \nAVERAGE: {average}\n------------------------------------")


def input_number_students():
    while True:
        try:
            amount_students = int(input("Enter the number of students\n"))
            if amount_students < 0:
                raise IndexError
            else:
                return amount_students
        except IndexError:
            output_in_CLI("Error, must be a positive number")
        except ValueError as error:
            print(f"Error, invalid value must be a int: {error}")


def input_student_note(subject):
    while True:
        try:
            note = int(input(f"Enter the note of {subject}\n"))
            if note > 100 or note < 1:
                raise IndexError
            else:
                return round(note)
        except IndexError:
            output_in_CLI("Error, the note must be between 1 and 100")
        except ValueError as error:
            print(f"Error, invalid value: {error}")


def output_in_CLI(text):
    print(text)