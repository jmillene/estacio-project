from flask import jsonify, request
from service.get_users import list_users

def get_users():
    name = request.args.get('name')
    email = request.args.get('email')
    
    print(f"Received name: {name}")
    print(f"Received email: {email}")
    
    if not name and not email:
        return jsonify({"message": "Nome ou email não fornecidos."}), 400
    
    try:
        users = list_users(name, email)
        print(f"Users found: {users}")
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
