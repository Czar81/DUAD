from flask import request, jsonify
from flask.views import View
from scripts.database.user_repository import UserRepository
from psycopg2 import IntegrityError, DataError, OperationalError, InterfaceError


class UserView(View):

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def post(self):
        try:
            request_body = request.json
            message, response = self.user_repo.create_user(
                name=request_body["name"],
                email=request_body["email"],
                username=request_body["username"],
                password=request_body["password"],
                birthday=request_body["birthday"]
            )
            return jsonify({"message":message}), response
        except KeyError as e:
            return jsonify({"message":f"Request key does not exist: {e}"}), 400
        except IntegrityError as e:
            return jsonify({"message":f"Username or email already exists: {e}"}), 409
        except DataError as e:
            return jsonify({"message":f"Invalid data format: {e}"}), 422 
        except OperationalError as e:
            return jsonify({"message":f"Database operation failed: {e}"}) , 503      
        except InterfaceError as e:
            return jsonify({"message":f"Error trying to communicate with db: {e}"}), 500
        except Exception as e:
            return jsonify({"message":f"Unexpected error occurred: {e}"}), 500
    
    def put(self, id):
        try:
            new_state = request.json['state']
            self.user_repo.chage_user_state(id, new_state)
        except KeyError as e:
            return jsonify({"message":f"State key does not exist: {e}"}), 400
        except DataError as e:
            return jsonify({"message":f"Invalid data format: {e}"}), 422 
        except OperationalError as e:
            return jsonify({"message":f"Database operation failed: {e}"}) , 503      
        except InterfaceError as e:
            return jsonify({"message":f"Error trying to communicate with db: {e}"}), 500
        except Exception as e:
            return jsonify({"message":f"Unexpected error occurred: {e}"}), 500
    
    def get(self, id):