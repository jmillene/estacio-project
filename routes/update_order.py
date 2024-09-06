from flask import Blueprint
from controller.update_order import update_order

update_order_bp = Blueprint('update_order', __name__)

@update_order_bp.route('/<int:order_id>', methods=['PUT'])
def update_order_route(order_id):
    return update_order(order_id)
