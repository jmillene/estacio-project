from flask import Blueprint
from controller.update_users import update_user_endpoint

update_user_bp = Blueprint('update_user', __name__)

@update_user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    return update_user_endpoint(user_id)
