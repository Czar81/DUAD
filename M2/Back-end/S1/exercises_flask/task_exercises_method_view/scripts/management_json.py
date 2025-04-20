import json

def import_json(path="data/tasks.json"):
    """
    Imports and reads JSON data from specified file path.
    Returns tuple with (data list, error message if any, HTTP status code).
    """
    tasks_list=[]
    try: 
        # Open and read JSON file from given path
        with open(path, mode="r", newline="", encoding="UTF-8") as file:
            tasks_list = json.load(file)
        # Return success when there was not an error
        return tasks_list, None, 200
    except FileNotFoundError as error:
         # Handle file not found
        return [], f"file not found: {error}", 500
    except Exception as error:
        # Handle unexpected errors
        return [], f"An unexpected error occurred tryig to import json: {error}", 500


def export_json(
        path_export="data/tasks.json", 
        path_import="data/tasks.json", 
        new_task_list=[], 
        export_all=False):
    """
    Exports task data to JSON file, either appending new tasks or overwriting entirely.
    Returns tuple with (success status, error message if any, HTTP status code).
    """
    try:
        # Check if export_all is True
        if export_all:
            # Overwrite tasks
            with open(path_export, mode="w", encoding="UTF-8")as file:
                json.dump(new_task_list, file, indent=4)
            return True, None, 201
        else:
            # Import existing tasks
            task_list, message, response = import_json(path_import)
            # Check error from importing 
            if not task_list:
                return False, message, response
            # Append new task to tasks json
            task_list.append(new_task_list)
            # Write the file
            with open(path_export, mode="w", encoding="UTF-8") as file:
                json.dump(task_list, file, indent=4)
            return True, None, 201
    except Exception as error:
        # Handle unexpected errors
        return False,f"An unexpected error occurred trying to export task: {error}", 500


def update_task(task_id, updated_task, path="data/tasks.json"):
    """
    Updates specific task in JSON file by task ID.
    Returns tuple with (success status, error message if any, HTTP status code).
    """
    new_tasks = []
    try:
        # Import existing tasks
        tasks, message, response = import_json(path)
        # Check error from importing 
        if not tasks:
            return False, message, response 
        # Filter tasks by id
        new_tasks = [task for task in tasks if task["id"] != int(task_id)]
        # Append updated task to tasks
        new_tasks.append(updated_task)
        # Export new tasks
        verified, message, response = export_json(new_task_list=new_tasks, 
                                                  export_all=True, 
                                                  path_export=path,
                                                  path_import=path)
        # Check error from exporting 
        if not verified:
            return False, message, response
        return True, None, 200
    except Exception as error:
        # Handle unexpected errors
        return False, f"An unexpected error occurred trying to update json: {error}", 500


def remove_task(task_id, path="data/tasks.json"):
    """
    Removes specific task from JSON file by task ID.
    Returns tuple with (success status, error message if any, HTTP status code).
    """
    try:
        # Import existing tasks
        tasks, message, response = import_json(path)
        # Check error from importing 
        if not tasks:
            return False, message, response
        # Filter tasks by id
        new_tasks = [task for task in tasks if task["id"] != int(task_id)]
        # Export tasks without task deleted
        verified, message, response = export_json(new_task_list=new_tasks, 
                                                  export_all=True, 
                                                  path_export=path,
                                                  path_import=path)
        # Check error from exporting 
        if not verified:
            return False, message, response
        return True, None, 200
    except Exception as error:
        # Handle unexpected errors
        return False, f"An unexpected error occurred trying to remove task: {error}", 500
