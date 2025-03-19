import FreeSimpleGUI as fsg
from interface_new_category import _make_new_category_interface
from interface_new_expenses import _make_new_expenses_interface
from interface_new_revenues import _make_new_revenues_interface

def make_main_interface(data):
    try:
        # ------ Window Layout ------
        layout = [
            [fsg.Button("New Category"), fsg.Button("New Expenses"), fsg.Button("New Revenues")],
            [fsg.Table(
                values = data, 
                headings =  ["Title", "Amount", "Category"], 
                max_col_width = 10, 
                background_color=0xD9D9D9,
                auto_size_columns=False,
                justification="center",
                key="-TABLE-",
                tooltip="This is a table"
                )]
            ]
        # ------ Create Window ------
        window = fsg.Window('Personal Finance Management', layout)

        # ------ Event Loop ------
        while True:
            event, value = window.read()
            if event is None:
                break
            if event == "New Category":
                _make_new_category_interface()
            elif event == "New Expenses":
                _make_new_expenses_interface()
            elif event == "New Revenues":
                _make_new_revenues_interface()

        window.close()
    # Find correct tipy for this
    except Exception as error:
        # Change to display mesessage
        print(f"An unexpected error ocurred trying to display Main Interface: {error}")


def __load_data_table():
    pass

if __name__ == "__main__":
    make_main_interface([["Blasphemus",10000,"Games"], 
                         ["Half life", 2000, "Games"]])