from flask import Blueprint
from controller.update_products import update_product_endpoint

update_product_bp = Blueprint('update_product', __name__)

@update_product_bp.route('/update_product/<int:product_id>', methods=['PUT'])

def update_product_route(product_id):
    return update_product_endpoint(product_id)