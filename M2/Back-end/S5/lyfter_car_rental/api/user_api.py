from flask import request, jsonify
from flask.views import MethodView
from psycopg2 import IntegrityError, DataError, OperationalError, InterfaceError


class UserView(MethodView):

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def post(self):
        try:
            request_body = request.json
            response = self.user_repo.create_user(
                name=request_body["name"],
                email=request_body["email"],
                username=request_body["username"],
                password=request_body["password"],
                birthday=request_body["birthday"]
            )
            return jsonify({"message":"User created successfully"}), response
        except KeyError as e:
            return jsonify({"message":f"Request key does not exist: {e}"}), 400
        except IntegrityError:
            return jsonify({"message":f"Username or email already exists"}), 409
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
            if new_state == "Debtor":
                response=self.user_repo.put_user_debtor(id)
            else:
                response = self.user_repo.change_user_state(id, new_state)
            return jsonify({"message": "User state changed successfully"}), response
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
    
    def get(self):
        try:
            request_body = dict(request.args)
            if request_body != {}:
                results, response = self.user_repo.get_users_by_filters(**request_body)
            elif request_body == {}:
                results, response = self.user_repo.get_all_users()
            return jsonify({"return":results}), response
        except KeyError as e:
            return jsonify({"message":f"Request keys do not exist: {e}"}), 400
        except DataError as e:
            return jsonify({"message":f"Invalid data format: {e}"}), 422 
        except OperationalError as e:
            return jsonify({"message":f"Database operation failed: {e}"}) , 503      
        except InterfaceError as e:
            return jsonify({"message":f"Error trying to communicate with db: {e}"}), 500
        except Exception as e:
            return jsonify({"message":f"Unexpected error occurred: {e}"}), 500
        