import FreeSimpleGUI as fsg
from interface_new_category import _make_new_category_interface
from interface_new_expenses import _make_new_expenses_interface
from interface_new_revenues import _make_new_revenues_interface

def make_main_interface(data):
    # ------ Constants ------
    light_blue="#4A5C6A"
    gray="#D9D9D9"
    dark_blue="#11212D"
    font = ("Helvatica", 12, "bold")

    try:
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
                       border_width=0)
                ],
            [fsg.Table(
                values = data, 
                headings =  ["Title", "Amount", "Category"], 
                background_color=gray,
                sbar_background_color=gray,
                header_background_color=gray,
                auto_size_columns=False,
                justification="center",
                key="-TABLE-",
                tooltip="This is a table",
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
            if event == "New Category":
                _make_new_category_interface()
            elif event == "New Expenses":
                _make_new_expenses_interface()
            elif event == "New Revenues":
                _make_new_revenues_interface()

        window.close()
    # Find correct tipy for this
    except Exception as error:
        fsg.popup_error(f"An unexpected error ocurred trying to display Main Interface: {error}")


def __load_data_table():
    pass

if __name__ == "__main__":
    make_main_interface([["Blasphemous",10_000,"Games"], ["Half life", 2_000, "Games"]])