from flask import Blueprint
from controller.delete_users import delete_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/delete_users', methods=['DELETE'])
def delete_users():
    return delete_user()