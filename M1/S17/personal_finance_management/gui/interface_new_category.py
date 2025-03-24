import FreeSimpleGUI as fsg
from utils.export_csv import export_category

def _make_new_category_interface():
    """
    Creates a modal window for adding new category
    """
    # ------ Constants ------
    light_blue="#4A5C6A"
    gray="#D9D9D9"
    dark_blue="#11212D"
    font = ("Helvetica", 20, "bold")
    try:
        # ------ Window Layout ------
        layout = [
            # Title
            [fsg.Text(text="Enter new category", 
                      text_color=gray, 
                      background_color=light_blue)],
            # Input
            [fsg.Input(background_color=gray,
                       text_color="#4A5C6A",
                       border_width=0,
                       key="-CATEGORY-", 
                       size=(20, 1)), 
            # Button
            fsg.Button(button_text="Create", 
                       button_color=dark_blue, 
                       border_width=0)]
        ]

        # ------ Create Window ------
        window = fsg.Window(title="New Category",
                            background_color=light_blue,
                            font=font,
                            modal=True,
                            layout=layout)

        # ------ Event Loop ------
        while True:
            event, value = window.read()
            # Window closed event
            if event == fsg.WIN_CLOSED:
                break
            # Create button event
            elif event == "Create":    
                export_category(new_category=value["-CATEGORY-"])
                window.close()

        # Cleanup on window close        
        window.close()

    # Catch-all for unexpected errors
    except Exception as error:
        fsg.popup_error(f"An unexpected error ocurred trying to display New Category: {error}", title="Erro in New Category")