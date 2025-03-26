import FreeSimpleGUI as fsg
from gui.interface_new_category import _make_new_category_interface
from gui.interface_new_expenses import _make_new_expenses_interface
from gui.interface_new_revenues import _make_new_revenues_interface
from utils.import_csv import import_data_table_csv

def make_main_interface():
    """
    Creates and manages the main application interface for Personal Finance Management.
    Handles window layout, event loop, and error handling for the primary application window.
    """
    
    # ------ Constants ------
    # Color scheme and font settings for consistent styling
    light_blue = "#4A5C6A"  
    gray = "#D9D9D9"        
    dark_blue = "#11212D"    
    font = ("Helvetica", 20, "bold") 
    try:
        
        # ------ Data Loading ------
        data_import = import_data_table_csv()
        
        # ------ Window Layout Definition ------
        layout = [
            # Button row for main actions
            [fsg.Button(button_text="New Category", 
                       button_color=dark_blue,
                       border_width=0,
                       tooltip="Add new spending categories"),
             fsg.Button(button_text="New Expenses", 
                       button_color=dark_blue,
                       border_width=0,
                       tooltip="Record new expenses"),
             fsg.Button(button_text="New Revenues", 
                       button_color=dark_blue,
                       border_width=0,
                       tooltip="Record new income")],
            
            # Data table displaying all transactions
            [fsg.Table(
                values=data_import, 
                headings=["Title", "Amount", "Category"], 
                key="-TABLE-", 
                background_color=gray,
                sbar_background_color=gray,
                header_background_color=gray,
                auto_size_columns=False,
                justification="center",
                text_color=light_blue,                
                def_col_width=11, 
                header_text_color=light_blue,
                border_width=0,     
                header_border_width=1,
                )]
        ]
        
        # ------ Window Creation ------
        window = fsg.Window(
            title="Personal Finance Management",
            background_color=light_blue,
            font=font,
            element_justification="center",
            layout=layout,
        )

        # ------ Event Loop ------
        while True:
            event, value = window.read()
            # Window closed event
            if event == fsg.WIN_CLOSED:
                break 
            # New Category button handler
            elif event == "New Category":
                _make_new_category_interface()
                window["-TABLE-"].Update(import_data_table_csv())
            elif event == "New Expenses":
                _make_new_expenses_interface()
                window["-TABLE-"].Update(import_data_table_csv())        
            # New Revenues button handler
            elif event == "New Revenues":
                _make_new_revenues_interface()
                window["-TABLE-"].Update(import_data_table_csv())


        # Cleanup on window close
        window.close()
        
    except Exception as error:
        # Catch-all for unexpected errors
        fsg.popup_error(f"An unexpected error ocurred trying to display Main Interface: {error}", title="Error in Main Interface")
