import FreeSimpleGUI as fsg

def _make_new_category_interface():
    # ------ Constants ------
    light_blue="#4A5C6A"
    gray="#D9D9D9"
    dark_blue="#11212D"
    font = ("Helvatica", 12, "bold")
    try:
        # ------ Window Layout ------
        layout = [
            [fsg.Text(text="Enter new category", 
                      text_color=gray, 
                      background_color=light_blue)],
            [fsg.Input(background_color=gray,
                       text_color="#4A5C6A",
                       border_width=0, 
                       size=(20, 1)), 
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
            event, values = window.read()
            if event is None:
                break
            elif event is "Create":
                pass
            

        window.close()
    # Find correct tipy for this
    except Exception as error:
        fsg.popup_error(f"An unexpected error ocurred trying to display New Category: {error}")