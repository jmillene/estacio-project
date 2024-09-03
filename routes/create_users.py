from flask import Blueprint
from controller.create_users import add_user

create_user_bp= Blueprint('user', __name__)

@create_user_bp.route('/create', methods=['POST'])
def create_users():
    return add_user()