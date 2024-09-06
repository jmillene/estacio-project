from flask import jsonify
from service.delete_item_order import delete_order_item

def delete_order_item_controller(order_id, product_id):
    result = delete_order_item(order_id, product_id)
    if result:
        return jsonify({"message": "Item removido da ordem com sucesso"}), 200
    else:
        return jsonify({"message": "Ordem ou item não encontrado"}), 404
