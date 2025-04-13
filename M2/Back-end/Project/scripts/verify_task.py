from scripts.management_json import import_json

def verify(request):
    """
    Main verification function that checks request validity through multiple steps.
    Returns a tuple with (success status, message, HTTP status code).
    """
    try:
        # Check blank spaces in request fields
        verified, message =__verify_blank_spaces(request)
        if not verified:
            return False, message, 400
        
        # Check the state field has valid values
        verified, message =__verify_states(request["state"])
        if not verified:
            return False, message, 400
        
        # Check the ID is unique
        verified, message, response =__verify_id(request["id"])
        if not verified:
            return False, message, response
        
        # If all checks pass
        return True, None, 200
    except Exception as error:
        # Handle unexpected errors
        return False, f"An unexpected error occured in verify: {error}", 500

    
def __verify_blank_spaces(request):
    """
    Checks that no fields in the request are empty or contain only whitespace.
    Returns tuple with (success status, error message if any).
    """
    try:
        # Check each key in the request
        for key, value in request.items():
            # Check if is None
            if value is None:
                raise TypeError(f"invalid request blank space in {key}")
            # Check if is blank
            elif not str(value).strip():
                raise ValueError(f"invalid request blank space in {key}")
            
        # If all goes good
        return True, None
    except ValueError as error:
        return False, error
    except KeyError as error:
        return False, f"could not found key from request: {error}"
    except TypeError as error:
        return False, error
    except Exception as error:
        # Handle unexpected errors
        return False, f"An unexpected error occured in __verify_blank_spaces: {error}"


def __verify_states(state):
    """
    Validates that the state field contains one of the allowed values.
    Returns tuple with (success status, error message if any).
    """
    try:
        # Check state is a string 
        if not isinstance(state,str):
            raise TypeError("state not string")
        # Check state has valid value
        if state.lower() in ["ready", "in progress", "pending"]:
            return True, None
        else:
            raise ValueError("invalid state")
    except TypeError as error:
        return False, error
    except ValueError as error:
        return False, error
    except Exception as error:
        # Handle unexpected errors
        return False, f"An unexpected error occured in __verify_states {error}"


def __verify_id(id):
    """
    Checks that the ID is an integer and unique (not existing in JSON data).
    Returns tuple with (success status, error message if any).
    """
    try:
        # Check ID is an integer
        if not isinstance(id, int):
            raise TypeError("id not a int")
        
        # Import tasks from JSON file
        tasks, message, response = import_json()
        # Check error from importing
        if not tasks:
                return False, message, response
        
        # Check for ID uniqueness
        for task in tasks:
            if task["id"] == id:
                raise ValueError(f"id ({id}) not unique")
        # If all goes good
        return True, None
    except ValueError as error:
        return False, error, 409
    except ImportError as error:
        return False, f"Error trying to import import_json", 500
    except TypeError as error:
        return False, error, 400
    except Exception as error:
        # Handle unexpected errors
        return False, f"An unexpected error occured in __verify_id {error}", 500
