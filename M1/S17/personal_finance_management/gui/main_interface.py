import FreeSimpleGUI as fsg

def make_main_interface(data, headings):
    # ------ Window Layout ------
    layout = [
        [fsg.Button("New Category"), fsg.Button("New Expenses"), fsg.Button("New Revenues")],
        [fsg.Table(
            values = data, 
            headings = headings, 
            max_col_width = 10, 
            background_color=0xD9D9D9,
            auto_size_columns=True,
            justification="center",
            key="-TABLE-",
            tooltip="This is a table"
            )]
        ]
    # ------ Create Window ------
    window = fsg.Window('Personal Finance Management', layout)

    # ------ Event Loop ------
    while True:
        event, values = window.read()
        if event is None:
            break
        if event == "New Category":
            pass
        elif event == "New Expenses":
            pass
        elif event == "New Revenues":
            pass

    window.close()

if __name__ == "__main__":
    make_main_interface([["Blasphemus",10000,"Games"], ["Half life", 2000, "Games"]], ["Titulo", "Monto", "Categoria"])