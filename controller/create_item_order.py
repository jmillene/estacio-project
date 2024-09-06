from flask import jsonify, request
from service.create_item_order import create_order_item

def create_order_item_endpoint(order_id):
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or not quantity:
        return jsonify({"message": "Campos obrigatórios não fornecidos"}), 400

    result, status_code = create_order_item(order_id, product_id, quantity)
    return jsonify(result), status_code
