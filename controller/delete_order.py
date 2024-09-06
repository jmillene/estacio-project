from flask import jsonify
from service.delete_order import delete_order


def delete_order_by_id(order_id):
    result = delete_order(order_id)
    if result:
        return jsonify({"message": "Ordem deletada com sucesso"}), 200
    else:
        return jsonify({"message": "Ordem não encontrada"}), 404