from flask import Blueprint
from controller.update_item_order import update_order_item_endpoint

update_order_items_bp = Blueprint('update_item_order', __name__)

@update_order_items_bp.route('/item_order/<int:item_id>/items', methods=['PUT'])
def update_order_item_route(item_id):
    return update_order_item_endpoint(item_id)
