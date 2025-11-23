from flask import request, jsonify
from .encoding import JWT_Manager
from src.db.user_module.db_user_manager import DbUserManager
from functools import wraps

jwt_manager = JWT_Manager()


def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return jsonify(message="Missing token"), 401
            try:
                token = token.replace("Bearer ", "")
                id_decoded = jwt_manager.decode(token)
                role = DbUserManager.get_user_role_by_id(id_decoded["id"])
                if role not in allowed_roles:
                    return jsonify(message="Unauthorized"), 403
                kwargs["id_user"] = id_decoded["id"]
                kwargs["role"] = role
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify(message="Invalid token"), 401

        return wrapper

    return decorator


def validate_fields(required=None, optional=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            required_fields = required or []
            optional_fields = optional or []

            if not required_fields and not optional_fields:
                return func(*args, **kwargs)

            data = request.get_json() or {}

            if required_fields:
                if not data:
                    return jsonify(message="Missing body"), 400

                missing = [f for f in required_fields if data.get(f) is None]
                if missing:
                    return (
                        jsonify(
                            message=f"Missing required fields: {', '.join(missing)}"
                        ),
                        400,
                    )

            for field in required_fields:
                kwargs[field] = data.get(field)

            for field in optional_fields:
                if data.get(field) is not None:
                    kwargs[field] = data.get(field)

            return func(*args, **kwargs)

        return wrapper

    return decorator
