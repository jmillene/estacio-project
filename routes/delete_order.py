from flask import Blueprint
from controller.delete_order import delete_order_by_id

delete_order_bp = Blueprint('delete_order', __name__)

@delete_order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order_route(order_id):
    return delete_order_by_id(order_id)