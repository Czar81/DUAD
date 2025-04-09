from flask import Flask, request, jsonify
from scripts.management_json import import_json, export_json, update_task, remove_task
from scripts.verify_task import verify
app = Flask(__name__)

@app.route("/")
def root():
    return f"""<h1>Index Task</h1>
    <p>
        <ul>
            <li><a href="/make_task"> Create a new task</a></li>
            <li><a href="/tasks">See all task</a></li>
            <li><a href="/change_task/{id}">Change an existed task</a></li>
            <li><a href="/delate_task/{id}">Delate_task</a></li>
        </ul>
    </p>"""


@app.route("/make_task", methods=["POST"])  
def post_task():
    request_body = request.json
    verified, message, response = verify(request_body)
    if not verified:
        return jsonify({"message" : message}), response
    verified, message, response = export_json(new_task_list=request_body)
    if verify:
        return jsonify({"request_body":request_body}), response
    else:
        return jsonify({"message" : message}), response


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks_list, message, response = import_json()
    if not tasks_list:
        return jsonify(message), response
    try:
        state_filter = request.args.get("state")
        if state_filter:
            filtered_tasks = list(
                filter(lambda task: task["state"] == state_filter, tasks_list)
                )
            return jsonify({"data": filtered_tasks}), response
        return jsonify(tasks_list), response
    except ValueError as error:
        return jsonify(f"invalid state input: {error}"), 400
    except Exception as error:
        return jsonify(f"unexpected error occured trying to get tasks"), 500
        


@app.route("/change_task/<id>", methods=["PUT", "PATCH"])
def put_task(id):
    updated_task = request.json
    new_updated_task = update_task(id, updated_task)
    return jsonify({"request_body":new_updated_task}), 200


@app.route("/delete_task/<id>", methods=["DELETE"])
def delete_task(id):
    remove_task(id)
    return jsonify({"message": f"Task {id} deleted"}), 200

def start():
    app.run(host="localhost", debug=True)