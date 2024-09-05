from flask import Blueprint
from controller.delete_product import delete_product_endpoint

delete_product_bp = Blueprint('delete_product', __name__)

@delete_product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    return delete_product_endpoint(product_id)