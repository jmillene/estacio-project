from flask import Blueprint
from controller.create_product import add_product

create_product_bp= Blueprint('product', __name__)

@create_product_bp.route('/create', methods=['POST'])
def create_products():
    return add_product()