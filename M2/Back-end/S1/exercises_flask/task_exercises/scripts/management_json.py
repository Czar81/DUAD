import json

def import_json(path="data/tasks.json"):
    tasks_list=[]
    try: 
        with open(path, mode="r", newline="", encoding="UTF-8") as file:
            tasks_list = json.load(file)
        return tasks_list
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return []

def export_json(path_export="data/tasks.json", path_import="data/tasks.json", new_task_list=[]):
    try:
        if not new_task_list:
            raise Exception #Change 
        task_list = import_json(path_import)
        task_list.append(new_task_list)
        with open(path_export, mode="w", encoding="UTF-8") as file:
            json.dump(task_list, file, indent=4)
    except Exception as error:
        print(f"An unexpected error occurred: {error}")