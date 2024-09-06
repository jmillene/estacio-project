from flask import Blueprint, jsonify
from controller.get_order import get_order_by_id

list_orders_bp = Blueprint('list_order', __name__)

@list_orders_bp.route('/list_orders', methods=['GET'])
def list_orders():
   return get_order_by_id
