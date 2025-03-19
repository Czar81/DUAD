import FreeSimpleGUI as fsg

def _make_new_revenues_interface():
    try:
        # ------ Window Layout ------
        layout = [
            [fsg.Text(text="Enter Title")],
            [fsg.Input()], 
            [fsg.Text(text="Enter Amount")],
            [fsg.Input()], 
            [fsg.Text(text="Enter Category")],
            [fsg.Input()], 
            [fsg.Button(button_text="Create")]
        ]

        # ------ Create Window ------
        window = fsg.Window(title="New Revenues", layout=layout)

        # ------ Event Loop ------
        while True:
            event, values = window.read()
            if event is None:
                break  

        window.close()
    # Find correct tipy for this
    except Exception as error:
        # Change to display mesessage
        print(f"An unexpected error ocurred trying to display New Revenues: {error}")