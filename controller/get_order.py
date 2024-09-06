from flask import jsonify
from service.get_orders import get_order


def get_order_by_id(order_id):
    result = get_order(order_id)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"message": "Ordem não encontrada"}), 404