from flask import jsonify
from service.delete_product import delete_product

def delete_product_endpoint(product_id):
    try:
        result = delete_product(product_id)
        if result:
            return jsonify({"message": "Produto deletado com sucesso."}), 200
        else:
            return jsonify({"message": "Produto não encontrado."}), 404
    except Exception as e:
        print(f"Erro ao deletar produto: {e}")  # Log de depuração
        return jsonify({"message": str(e)}), 500
