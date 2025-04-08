from scripts.management_json import import_json

def verify(request):
    try:
        verified, key =__verify_blank_spaces(request)
        if not verified:
            return False, f"invalid request blank space in {key}"
        elif not __verify_states(request["state"]):
            return False, "invalid state of the task"
        elif not __verify_id(request["id"]):
            return False, "invalid id"
        return True, None
    except Exception as error:
        print(f"An unexpected error occured in verify: {error}")
        return False, "invalid request"

    
def __verify_blank_spaces(request):
    try:
        for key, value in request.items():
            if value is None:
                return False, key
            elif not str(value).strip():
                return False, key
        return True, None
    except Exception as error:
        print(f"An unexpected error occured in __verify_blank_spaces: {error}")


def __verify_states(state):
    try:
        if not isinstance(state,str):
            return False
        if state.lower() in ["ready", "in progress", "pending"]:
            return True
        else:
            return False 
    except Exception as error:
        print(f"An unexpected error occured in __verify_states {error}")
        return False


def __verify_id(id):
    try:
        if not isinstance(id, int):
            return False
        tasks = import_json()
        for task in tasks:
            if task["id"] == id:
                return False
        return True
    except Exception as error:
        print(f"An unexpected error occured in __verify_id {error}")
        return False
