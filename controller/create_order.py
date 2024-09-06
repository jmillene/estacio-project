from flask import jsonify, request
from service.create_order import create_order

def add_order():
    data = request.get_json()
    user_id = data.get('user_id')
    
    if not user_id:
        return jsonify({"mensagem": "ID do usuário requerido"}), 400
    
    result = create_order(user_id)
    return jsonify(result), 201
