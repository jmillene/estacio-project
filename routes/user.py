from flask import Blueprint
from controller.user import add_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/create', methods=['POST'])
def create_user():
    return add_user()
