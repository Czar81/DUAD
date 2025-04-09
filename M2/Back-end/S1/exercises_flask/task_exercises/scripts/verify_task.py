from scripts.management_json import import_json

def verify(request):
    try:
        verified, message =__verify_blank_spaces(request)
        if not verified:
            return False, message, 400
        verified, message =__verify_states(request["state"])
        if not verified:
            return False, message, 400
        verified, message =__verify_id(request["id"])
        if not verified:
            return False, message, 409
        return True, None, 200
    except Exception as error:
        return False, f"An unexpected error occured in verify: {error}", 500

    
def __verify_blank_spaces(request):
    try:
        for key, value in request.items():
            if value is None:
                raise TypeError(f"invalid request blank space in {key}")
            elif not str(value).strip():
                raise ValueError(f"invalid request blank space in {key}")
        return True, None
    except ValueError as error:
        return False, error
    except KeyError as error:
        return False, f"could not found key from request: {error}"
    except TypeError as error:
        return False, error
    except Exception as error:
        return False, f"An unexpected error occured in __verify_blank_spaces: {error}"


def __verify_states(state):
    try:
        if not isinstance(state,str):
            raise TypeError("state not string")
        if state.lower() in ["ready", "in progress", "pending"]:
            return True, None
        else:
            raise ValueError("invalid state")
    except TypeError as error:
        return False, error
    except ValueError as error:
        return False, error
    except Exception as error:
        return False, f"An unexpected error occured in __verify_states {error}"


def __verify_id(id):
    try:
        if not isinstance(id, int):
            raise TypeError("id not a int")
        tasks, message, response = import_json()
        for task in tasks:
            if task["id"] == id:
                raise ValueError(f"{id} not unique")
        return True, None
    except ValueError as error:
        return False, error
    except ImportError as error:
        return False, f"Error trying to import import_json"
    except TypeError as error:
        return False, error
    except Exception as error:
        return False, f"An unexpected error occured in __verify_id {error}"
