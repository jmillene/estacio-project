from flask import Blueprint
from controller.create_users import add_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/create', methods=['POST'])
def create_users():
    return add_user()
