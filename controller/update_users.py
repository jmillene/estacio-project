from flask import jsonify, request
from service.update_users import update_user

def update_user_endpoint(user_id):
    data = request.get_json()  # Obtém dados do corpo da requisição
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({"message": "Name, email, and password are required."}), 400

    try:
        print(f"Updating user: id={user_id}, name={name}, email={email}, password={password}")  # Log de depuração
        result = update_user(user_id, name, email, password)
        return jsonify(result), 200
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")  # Log de depuração
        return jsonify({"message": str(e)}), 500
