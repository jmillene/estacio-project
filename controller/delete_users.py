from flask import jsonify
from service.delete_users import delete_user

def delete_user_endpoint(user_id):
    try:
        result = delete_user(user_id)
        if result:
            return jsonify({"message": "Usuário deletado com sucesso."}), 200
        else:
            return jsonify({"message": "Usuário não encontrado."}), 404
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")  # Log de depuração
        return jsonify({"message": str(e)}), 500
