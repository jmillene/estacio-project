from flask import Blueprint
from controller.delete_users import delete_user_endpoint

delete_user_bp = Blueprint('delete_user', __name__)

@delete_user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    return delete_user_endpoint(user_id)
