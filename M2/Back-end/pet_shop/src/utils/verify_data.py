from flask import request, jsonify
from .encoding import JWT_Manager
from src.db.db_user_manager import DbUserManager
from functools import wraps

jwt_manager = JWT_Manager()


def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return jsonify(message="Missing token"), 401
            token = token.replace("Bearer ", "")
            id_decoded = jwt_manager.decode(token)
            role = DbUserManager.get_user_role_by_id(id_decoded["id"])
            if role not in allowed_roles:
                return jsonify(message="Unauthorized"), 403
            kwargs["user_id"] = id_decoded["id"]
            return func(*args, **kwargs)

        return wrapper

    return decorator


def general_data_validation(allowed_roles, *required):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            data = request.get_json()
            if token == None:
                return jsonify(message="Missing token"), 401
            token = token.replace("Bearer ", "")
            try:
                id_decoded = jwt_manager.decode(token)
                role = DbUserManager.get_user_role_by_id(id_decoded["id"])
            except Exception:
                return jsonify(message="Invalid or expired token"), 401

            if role not in allowed_roles:
                return jsonify(message="Unauthorized"), 403
            if not data:
                return jsonify(message="Missing body"), 400

            missing = [field for field in required if data.get(field) is None]

            if missing:
                return jsonify(message=f"Missing fields: {', '.join(missing)}"), 400

            for field in required:
                kwargs[field] = data.get(field)
            kwargs["id_user"] = id_decoded["id"]
            return func(*args, **kwargs)

        return wrapper

    return decorator


def require_fields(*required):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            if not data:
                return jsonify(message="Missing body"), 400
            missing = [field for field in required if data.get(field) is None]
            if missing:
                return jsonify(message=f"Missing fields: {', '.join(missing)}"), 400
            for field in required:
                kwargs[field] = data.get(field)
            return func(*args, **kwargs)

        return wrapper

    return decorator
