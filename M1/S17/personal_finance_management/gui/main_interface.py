import FreeSimpleGUI as fsg
from gui.interface_new_category import _make_new_category_interface
from gui.interface_new_expenses import _make_new_expenses_interface
from gui.interface_new_revenues import _make_new_revenues_interface
from utils.import_csv import _import_data_table_csv

def make_main_interface():
    # ------ Constants ------
    light_blue="#4A5C6A"
    gray="#D9D9D9"
    dark_blue="#11212D"
    font = ("Helvatica", 20, "bold")

    # -- Options for Combo --
    options = []

    try:
        # ------ Load data ------
        data_import = __load_data_table()
        # -------- Advice -------
        fsg.popup(("Change path of the fuction __load_data_table"))
        # ------ Window Layout ------
        layout = [
            [fsg.Button(button_text="New Category", 
                        button_color=dark_blue,
                       border_width=0),
            fsg.Button(button_text="New Expenses", 
                       button_color=dark_blue,
                       border_width=0),
            fsg.Button(button_text="New Revenues", 
                       button_color=dark_blue,
                       border_width=0)],
            [fsg.Table(
                values = data_import, 
                headings =  ["Title", "Amount", "Category"], 
                background_color=gray,
                sbar_background_color=gray,
                header_background_color=gray,
                auto_size_columns=False,
                justification="center",
                text_color=light_blue,                
                def_col_width=11,
                header_text_color=light_blue,
                border_width=0,
                header_border_width=1
                )]
            ]
        # ------ Create Window ------
        window = fsg.Window(title="Personal Finance Management", 
                            background_color=light_blue,
                            font=font,
                            element_justification="center",
                            layout=layout)

        # ------ Event Loop ------
        while True:
            event, value = window.read()
            if event is None:
                break
            elif event == "New Category":
                _make_new_category_interface()
            elif event == "New Expenses":
                _make_new_expenses_interface()
            elif event == "New Revenues":
                _make_new_revenues_interface()

        window.close()
    # Find correct type for this
    except Exception as error:
        fsg.popup_error(f"An unexpected error ocurred trying to display Main Interface: {error}")


def __load_data_table():
    # Change to your path
    data_import = _import_data_table_csv("C:/Users/Aaron/VS/Lyfther/DUAD/M1/S17/personal_finance_management/exports/data.csv")
    return data_import