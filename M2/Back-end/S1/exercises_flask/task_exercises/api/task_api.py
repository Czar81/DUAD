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
    verified, message = verify(request_body)
    if not verified:
        return jsonify({"message" : message}), 400
    export_json(new_task_list=request_body)
    return {"request_body":request_body}


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks_list = import_json()
    state_filter = request.args.get("state")
    if state_filter:
        filtered_tasks = list(
            filter(lambda task: task["state"] == state_filter, tasks_list)
            )
        return {"data": filtered_tasks}
    return tasks_list


@app.route("/change_task/<id>", methods=["PUT", "PATCH"])
def put_task(id):
    updated_task = request.json
    new_updated_task = update_task(id, updated_task)
    return {"request_body":new_updated_task}


@app.route("/delete_task/<id>", methods=["DELETE"])
def delete_task(id):
    remove_task(id)
    return jsonify({"message": f"Task {id} deleted"}), 200

def start():
    app.run(host="localhost", debug=True)