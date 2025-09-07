from flask import Flask
from flask import jsonify, Response, request
from db.db_user_manager import DbUserManager
from db.db_receipt_manager import DbReceiptManager
from encoding import JWT_Manager

app = Flask("user-service")
db_user_manager = DbUserManager()
db_receipt_manager = DbReceiptManager()
jwt_manager =JWT_Manager("MyNameIsJeff","HS256")


@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = db_user_manager.insert_user(data.get('username'), data.get('password'))
        user_id = result[0]

        token = jwt_manager.encode({'id':user_id})
        
        return jsonify(token=token)
    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = db_user_manager.get_user(data.get('username'), data.get('password'))

        if(result == None):
            return Response(status=403)
        else:
            user_id = result[0]
            token = jwt_manager.encode({'id':user_id})
        
            return jsonify(token=token)

@app.route('/me', methods=["GET"])
def me():
    try:
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            user = db_user_manager.get_user_by_id(user_id)
            return jsonify(id=user_id, username=user[1])
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route("/me/receipts", methods=["GET"])
def get_user_receipt():
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            receipts = db_receipt_manager.get_receipt_by_user_id(user_id)
            return jsonify({"receipts":receipts}),200
        else:
            return Response(status=403)

def start_user_api():
    app.run(host="localhost",port=5002, debug=True)