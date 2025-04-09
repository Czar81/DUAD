import json

def import_json(path="data/tasks.json"):
    tasks_list=[]
    try: 
        with open(path, mode="r", newline="", encoding="UTF-8") as file:
            tasks_list = json.load(file)
        return tasks_list, None, 200
    except FileNotFoundError as error:
        return [], f"file not found: {error}", 500
    except Exception as error:
        return [], f"An unexpected error occurred tryig to import json: {error}", 500

def export_json(
        path_export="data/tasks.json", 
        path_import="data/tasks.json", 
        new_task_list=[], 
        export_all=False):
    try:
        if export_all:
            with open(path_export, mode="w", encoding="UTF-8")as file:
                json.dump(new_task_list, file, indent=4)
            return True, None, 201
        else:
            task_list, message, response = import_json(path_import)
            task_list.append(new_task_list)
            with open(path_export, mode="w", encoding="UTF-8") as file:
                json.dump(task_list, file, indent=4)
            return True, None, 201  
    except Exception as error:
        return False,f"An unexpected error occurred trying to export task: {error}", 500

def update_task(id, updated_task, path="data/tasks.json"):
    try:
        tasks = import_json(path)
        new_tasks = [task for task in tasks if task.get("id") != id]
        new_tasks.append(updated_task)
        export_json(new_task_list=new_tasks, export_all=True, path_export=path,path_import=path)
    except Exception as error:
        return False, f"An unexpected error occurred trying to update json: {error}", 500


def remove_task(id, path="data/tasks.json"):
    try:
        tasks = import_json(path)
        new_tasks = [task for task in tasks if task.get("id") != id]
        export_json(new_task_list=new_tasks, export_all=True, path_export=path,path_import=path)
    except Exception as error:
        return False, f"An unexpected error occurred trying to remove task: {error}", 500
