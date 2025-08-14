from flask import request, jsonify
from flask.views import MethodView
from psycopg2 import IntegrityError, DataError, OperationalError, InterfaceError


class CarRentalView(MethodView):

    def __init__(self, entity_repo):
        self.entity_repo = entity_repo

    def post(self):
        try:
            request_body = request.json
            response = self.entity_repo.create(request_body)
            return jsonify({"message":"Created successfully"}), response
        except ValueError as e:
            return jsonify({"message":str(e)}), 409
        except KeyError as e:
            return jsonify({"message":f"Request key does not exist: {str(e)}"}), 400
        except IntegrityError:
            return jsonify({"message":f"Some data already exists"}), 409
        except DataError as e:
            return jsonify({"message":f"Invalid data format: {str(e)}"}), 422 
        except OperationalError as e:
            return jsonify({"message":f"Database operation failed: {str(e)}"}) , 503      
        except InterfaceError as e:
            return jsonify({"message":f"Error trying to communicate with db: {str(e)}"}), 500
        except Exception as e:
            return jsonify({"message":f"Unexpected error occurred: {str(e)}"}), 500
    
    def put(self, id):
        try:
            print(request.path)
            new_state = request.json['state']
            if new_state == "Debtor":
                response=self.entity_repo.put_user_debtor(id)
            elif new_state == "Return":
                response=self.entity_repo.car_returned(id)
                return jsonify({"message":"Car return successfully"}), response
            else:
                response = self.entity_repo.change_state(id, new_state)
            return jsonify({"message": "State changed successfully"}), response
        except KeyError as e:
            return jsonify({"message":f"State key does not exist: {str(e)}"}), 400
        except DataError as e:
            return jsonify({"message":f"Invalid data format: {str(e)}"}), 422 
        except OperationalError as e:
            return jsonify({"message":f"Database operation failed: {str(e)}"}) , 503      
        except InterfaceError as e:
            return jsonify({"message":f"Error trying to communicate with db: {str(e)}"}), 500
        except Exception as e:
            return jsonify({"message":f"Unexpected error occurred: {str(e)}"}), 500
    
    def get(self):
        try:
            request_body = dict(request.args)
            if request_body != {}:
                results, response = self.entity_repo.get_by_filters(**request_body)
            elif request_body == {}:
                results, response = self.entity_repo.get_all()
            return jsonify({"return":results}), response
        except KeyError as e:
            return jsonify({"message":f"Request keys do not exist: {str(e)}"}), 400
        except DataError as e:
            return jsonify({"message":f"Invalid data format: {str(e)}"}), 422 
        except OperationalError as e:
            return jsonify({"message":f"Database operation failed: {str(e)}"}) , 503      
        except InterfaceError as e:
            return jsonify({"message":f"Error trying to communicate with db: {str(e)}"}), 500
        except Exception as e:
            return jsonify({"message":f"Unexpected error occurred: {str(e)}"}), 500
        