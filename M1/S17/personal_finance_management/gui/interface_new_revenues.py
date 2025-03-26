import FreeSimpleGUI as fsg
from utils.import_csv import import_data_category_csv
from utils.export_csv import export_movements

def _make_new_revenues_interface():
    """
    Creates and manages the interface for adding new revenue entries.
    """

    # ------ Constants ------
    # Color scheme and font settings for consistent styling
    light_blue="#4A5C6A"
    gray="#D9D9D9"
    dark_blue="#11212D"
    font = ("Helvetica", 20, "bold")

    try:
        # ------ Load data ------
        categories = import_data_category_csv()
        # ------ Window Layout ------
        layout = [
            # Title
            [fsg.Text(text="Enter Title",
                      text_color=gray,
                      background_color=light_blue)],
            [fsg.Input(background_color=gray,
                       text_color="#4A5C6A", 
                       border_width=0,
                       key="-TITLE-", 
                       size=(25, 1))], 
            # Amount
            [fsg.Text(text="Enter Amount",
                      text_color=gray,
                      background_color=light_blue)],
            [fsg.Input(background_color=gray,
                       text_color="#4A5C6A", 
                       border_width=0,
                       key="-AMOUNT-",
                       size=(25, 1))], 
            # Category
            [fsg.Text(text="Enter Category",
                      text_color=gray,
                      background_color=light_blue)],
            [fsg.Combo(values=categories,
                       background_color=gray,
                       text_color="#4A5C6A",
                       key="-CATEGORIES-",
                       readonly=True,
                       size=(25, 1))], 
            [fsg.Button(button_text="Create", 
                        button_color=dark_blue,
                        border_width=0)]
        ]

        # ------ Create Window ------
        window = fsg.Window(title="New Revenues",
                            background_color=light_blue,
                            font=font,
                            modal=True, 
                            layout=layout)

        # ------ Event Loop ------
        while True:
            event, values = window.read()
            # Window closed event
            if event == fsg.WIN_CLOSED:
                break  
            # Create button event
            elif event == "Create":
                movement = [values["-TITLE-"],values["-AMOUNT-"],values["-CATEGORIES-"]]
                export_movements(new_movement=movement)
                window.close()   

        # Cleanup on window close
        window.close()

    # Catch-all for unexpected errors
    except Exception as error:
        fsg.popup_error(f"An unexpected error ocurred trying to display New Revenues: {error}", title="Error in New Revenues")