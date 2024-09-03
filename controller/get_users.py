from flask import jsonify, request
from service.get_users import list_users

def get_users():
    name = request.args.get('name')
    email = request.args.get('email')
    
    try:
        result = list_users(name, email)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
