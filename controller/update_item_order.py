from flask import jsonify, request
from service.update_item_order import update_order_item

def update_order_item_endpoint(order_id):
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or not quantity:
        return jsonify({"message": "Campos obrigatórios não fornecidos"}), 400

    result, status_code = update_order_item(order_id, product_id, quantity)
    return jsonify(result), status_code
