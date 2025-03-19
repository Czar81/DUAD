import FreeSimpleGUI as fsg

def _make_new_expenses_interface():
    
    # ------ Window Layout ------
    layout = [
        [fsg.Text(text="Enter title")],
        [fsg.Input()], 
        [fsg.Text(text="Enter Amount")],
        [fsg.Input()], 
        [fsg.Text(text="Enter Category")],
        [fsg.Input()], 
        [fsg.Button(button_text="Create")]
    ]

    # ------ Create Window ------
    window = fsg.Window(title="New Expenses", layout=layout)

    # ------ Event Loop ------
    while True:
        event, values = window.read()
        if event is None:
            break  

    window.close()