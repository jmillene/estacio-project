from flask import Blueprint
from controller.get_users import get_users

list_users_bp = Blueprint('list_users', __name__)

@list_users_bp.route('/list_users', methods=['GET'])
def list_users_endpoint():
    return get_users()
