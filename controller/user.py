from flask import jsonify, request
from service.user import create_user

def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    if not name or not email or not password:
        return jsonify({"message": "Todos os campos são obrigatórios."}), 400
    
    try:
        create_user(name, email, password)
        return jsonify({"message": "Usuário criado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500

