from gui.main_interface import make_main_interface
from FreeSimpleGUI import popup

if __name__ == "__main__":
    try:
        make_main_interface() 
    except Exception as error:
        popup(f"An unexpected error ocurred: {error}")