from flask import jsonify, request
from service.user import create_user

def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({"message": "Nome e email são obrigatórios"}), 400
    
    try:
        create_user(name, email)
        return jsonify({"message": "Usuário adicionado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500

