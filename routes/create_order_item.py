from flask import Blueprint
from controller.create_item_order import create_order_item

create_order_item_bp = Blueprint('order_item', __name__)

@create_order_item_bp.route('/orders/<int:order_id>/items', methods=['POST'])

def order_item():
    return create_order_item
