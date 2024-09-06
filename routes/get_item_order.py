from flask import Blueprint
from controller.get_item_order import get_item_by_id

list_item_orders_bp = Blueprint('list_item_orders', __name__)

@list_item_orders_bp.route('/', methods=['GET'])
def list_item_orders_route():
    return get_item_by_id()
