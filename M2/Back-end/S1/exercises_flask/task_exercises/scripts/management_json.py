import json

def import_json(path="data/tasks.json"):
    tasks_list=[]
    try: 
        with open(path, mode="r", newline="", encoding="UTF-8") as file:
            tasks_list = json.load(file)
        return tasks_list
    except Exception as error:
        print(f"An unexpected error occurred tryig to import json: {error}")
        return []

def export_json(path_export="data/tasks.json", path_import="data/tasks.json", new_task_list=[], export_all=False):
    try:
        if not new_task_list:
            raise Exception #Change 
        if export_all:
            with open(path_export, mode="w", encoding="UTF-8")as file:
                json.dump(new_task_list, file, indent=4)
        else:
            task_list = import_json(path_import)
            task_list.append(new_task_list)
            with open(path_export, mode="w", encoding="UTF-8") as file:
                json.dump(task_list, file, indent=4)
    except Exception as error:
        print(f"An unexpected error occurred trying to export json: {error}")

def update_task(id, updated_task, path="data/tasks.json"):
    try:
        tasks = import_json(path)
        new_tasks = [task for task in tasks if task.get("id") != int(id)]
        new_tasks.append(updated_task)
        export_json(new_task_list=new_tasks, export_all=True, path_export=path,path_import=path)
    except Exception as error:
        print(f"An unexpected error occurred trying to export json: {error}")


def remove_task(id, path="data/tasks.json"):
    try:
        tasks = import_json(path)
        new_tasks = [task for task in tasks if task.get("id") != int(id)]
        export_json(new_task_list=new_tasks, export_all=True, path_export=path,path_import=path)
    except Exception as error:
        print(f"An unexpected error occurred trying to export json: {error}")