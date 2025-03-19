import FreeSimpleGUI as fsg

def _make_new_category_interface():
    try:
        # ------ Window Layout ------
        layout = [
            [fsg.Text(text="Enter new category")],
            [fsg.Input(), fsg.Button(button_text="Create")]
        ]

        # ------ Create Window ------
        window = fsg.Window(title="New Category", layout=layout)

        # ------ Event Loop ------
        while True:
            event, values = window.read()
            if event is None:
                break
            

        window.close()
    # Find correct tipy for this
    except Exception as error:
        # Change to display mesessage
        print(f"An unexpected error ocurred trying to display New Category: {error}")