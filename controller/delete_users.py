from flask import jsonify, request
from service.delete_users import delete_user

def delete_user_endpoint():
    user_id = request.args.get('id')
    
    if not user_id:
        return jsonify({"message": "ID do usuário não fornecido."}), 400
    
    try:
        result = delete_user(user_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
