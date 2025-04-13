from flask import Flask, request, jsonify, Response
from scripts.management_json import import_json, export_json, update_task, remove_task
from scripts.verify_task import verify

# Initializing Flask application
app = Flask(__name__)

# POST Method
@app.route("/make_task", methods=["POST"])  
def post_task():
    # Get JSON data from request body
    request_body = request.json
    # Call verification function to verify request
    verified, message, response = verify(request_body)
    # Check if there was an error
    if not verified:
        return jsonify({"message" : str(message)}), response
    verified, message, response = export_json(new_task_list=request_body)
    # Check if there was an error during export
    if verified: 
        return jsonify({"request_body":request_body}), response
    else: 
        return jsonify({"message" : str(message)}), response

# GET Method with optional state filtering
@app.route("/tasks", methods=["GET"])
def get_tasks():
    # Import tasks from JSON file
    tasks_list, message, response = import_json()
    # Check if task_list is empty
    if not tasks_list:
        return jsonify(message), response # Return error
    try:
        # Check for state filter in query parameters
        state_filter = request.args.get("state")
        if state_filter:
            # Filter tasks by state
            filtered_tasks = list(
                filter(lambda task: task["state"] == state_filter, tasks_list)
                )
            # Return filter tasks, with HTTP code
            return jsonify({"data": filtered_tasks}), response 
        # Return tasks without filter, with HTTP code
        return jsonify(tasks_list), response 
    except TypeError as error:
        # Handle invalid state input
        return jsonify(f"invalid state input: {str(error)}"), 400
    except Exception as error:
        # Handle unexpected errors
        return jsonify(f"unexpected error occured trying to get tasks"), 500
        

# PUT and PATCH Method
@app.route("/change_task/<task_id>", methods=["PUT", "PATCH"])
def put_task(task_id):
    # Get updated task data from request body
    updated_task = request.json
    # Verify updated task
    verified, message, response = verify(updated_task)
    if not verified:
        return jsonify({"message" : str(message)}), response
    # Update the taks by id with update_task()
    verified, message, response = update_task(task_id, updated_task)
    # Check if there was an error
    if verified:
        return jsonify({"request_body":updated_task}), response
    else:
        return jsonify({"message":str(message)}), response


# DELETE Method
@app.route("/delete_task/<id>", methods=["DELETE"])
def delete_task(task_id):
    # Call a function to delete a task by given id
    verified, message, response = remove_task(task_id)
    # Check if there was an error
    if verified:
        return jsonify({"message": f"Task {task_id} deleted"}), 200
    else:
        return jsonify({"message":str(message)}), response


# Function to start the Flask application
def start():
    app.run(host="localhost", debug=True)