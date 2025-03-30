from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/make_task", methods=["POST"])  
def post_task():
    request_body = request.json
    return {"request_body":request_body}

@app.route("/tasks")
def get_tasks():
    pass

@app.route("/change_task/<id>", methods=["PUT"])
def put_task(id):
    pass

@app.route("/delate_task/<id>", methods=["DELATE"])
def delate_task(id):
    pass

if __name__ == "__main__":
    app.run(host="localhost", debug=True)