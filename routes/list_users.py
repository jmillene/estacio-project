from flask import Blueprint
from controller.get_users import get_users

user_bp = Blueprint('user', __name__)

@user_bp.route('/list_users', methods=['GET'])
def list_users():
    return get_users()