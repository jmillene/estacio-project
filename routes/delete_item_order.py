from flask import Blueprint
from controller.delete_item_order import delete_order_item_controller

delete_order_items_bp = Blueprint('delete_order_items', __name__)

@delete_order_items_bp.route('/order/<int:order_id>/item/<int:product_id>', methods=['DELETE'])
def delete_order_item_route(order_id, product_id):
    return delete_order_item_controller(order_id, product_id)
