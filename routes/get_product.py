from flask import Blueprint, jsonify
from controller.get_product import fetch_products

list_products_bp = Blueprint('list_products', __name__)

@list_products_bp.route('/list_products', methods=['GET'])
def list_products():
    products, status_code = fetch_products()
    return jsonify(products), status_code
