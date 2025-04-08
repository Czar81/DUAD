from scripts.management_json import import_json
def verify(request):
    try:
        verified, key =__verify_blank_spaces(request)
        if not verified:
            return False, f"invalid request blank space in {key}"
        elif not __verify_states(request["state"]):
            return False, "invalid state of the task"
        elif not __verify_id(request["id"]):
            return False, "invalid id, id not uniquic"
        return True, None
    except Exception as error:
        print(f"An unexpected error occured in verify: {error}")
        return False, "invalid request"


def __verify_blank_spaces(request):
    try:
        for key, value in request.items():
            if not value:
                return False, key
            if not str(value).strip():
                return False, key
        return True, None
    except Exception as error:
        print(f"An unexpected error occured in __verify_blank_spaces: {error}")


def __verify_states(state):
    try:
        if state.strip().lower() in ["ready", "inprogress", "pending"]:
            return True
        else:
            return False 
    except Exception as error:
        print(f"An unexpected error occured in __verify_states {error}")


def __verify_id(id):
    try:
        tasks = import_json()
        for task in tasks:
            if task["id"] == id:
                return False
        return True
    except Exception as error:
        print(f"An unexpected error occured in __verify_id {error}")
