from flask import Flask, request, Blueprint

from ..service import registerService

bp = Blueprint('registerController', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def insert_user_data():
    username = registerService.register_user(request.get_json())
    return "Your register username is {}".format(username)