from flask import request, jsonify
from flask.views import MethodView
from psycopg2 import IntegrityError, DataError, OperationalError, InterfaceError


class CarView(MethodView):

    def __init__(self, car_repo):
        self.car_repo = car_repo

    def post(self):
        try:
            request_body = request.json
            response = self.car_repo.create_car(
                make=request_body["make"],
                model=request_body["model"],
                year=request_body["year"],
                state=request_body["state"],
            )
            return jsonify({"message":"Car created successfully"}), response
        except KeyError as e:
            return jsonify({"message":f"Request key does not exist: {e}"}), 400
        except IntegrityError:
            return jsonify({"message":f"carname or email already exists"}), 409
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
            response = self.car_repo.change_car_state(id, new_state)
            return jsonify({"message": "Car state changed successfully"}), response
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
                results, response = self.car_repo.get_cars_by_filters(**request_body)
            elif request_body == {}:
                results, response = self.car_repo.get_all_cars()
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
        