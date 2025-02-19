from utils import menu

def main():
    try:
        menu.menu_student_grade_control()
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()