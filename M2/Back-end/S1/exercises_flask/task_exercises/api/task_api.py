from flask import Flask, request, Response

app = Flask(__name__)
tasks_list=[{"id":1322,
            "title":"Homework English",
            "description":"Deep entire cave mail lose soon physical new count title leave cow opportunity sunlight dozen directly him record stared explain detail label plastic limited",
            "state":"in progress"},
            {"id":7272,
            "title":"Homework English",
            "description":"Deep entire cave mail lose soon physical new count title leave cow opportunity sunlight dozen directly him record stared explain detail label plastic limited",
            "state":"in progress"},
            {"id":9292,
            "title":"Homework English",
            "description":"Deep entire cave mail lose soon physical new count title leave cow opportunity sunlight dozen directly him record stared explain detail label plastic limited",
            "state":"ready"}]

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
    # Call function save data
    return {"request_body":request_body}


@app.route("/tasks", methods=["GET"])
def get_tasks():
    # Call function import data 
    filtered_tasks = tasks_list
    state_filter = request.args.get("state")
    if state_filter:
        filtered_tasks = list(
            filter(lambda task: task["state"] == state_filter, filtered_tasks)
            )
        return {"data": filtered_tasks}
    return tasks_list


@app.route("/change_task/<id>", methods=["PUT", "PATCH"])
def put_task(id):
    update_task = request.json
    # Call function to update a task
    return {"request_body":update_task}


@app.route("/delate_task/<id>", methods=["DELATE"])
def delate_task(id):
    delated_task = request.json
    # Call function to delate a task
    return {"delate_task":delated_task}


if __name__ == "__main__":
    app.run(host="localhost", debug=True)