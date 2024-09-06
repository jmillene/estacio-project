from flask import Blueprint
from controller.create_order import add_order

create_order_bp = Blueprint('create_order', __name__)

@create_order_bp.route('/create_order', methods=['POST'])
def create_order_route():
    return add_order()
