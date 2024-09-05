from flask import Flask
from routes.create_users import create_user_bp
from routes.get_users import list_users_bp
from routes.update_users import update_user_bp
from routes.delete_users import delete_user_bp 
from routes.create_product import create_product_bp
from routes.get_product import list_products_bp
from routes.update_products import update_product_bp
from routes.delete_product import delete_product_bp

from dotenv import load_dotenv

def create_app():
    # Carrega variáveis do arquivo .env
    load_dotenv()
    
    app = Flask(__name__)

    # Registra os blueprints
    app.register_blueprint(create_user_bp, url_prefix='/user')
    app.register_blueprint(list_users_bp, url_prefix='/user')
    app.register_blueprint(update_user_bp, url_prefix='/user')
    app.register_blueprint(delete_user_bp, url_prefix='/user')
    app.register_blueprint(create_product_bp, url_prefix='/product')
    app.register_blueprint(list_products_bp, url_prefix='/product')
    app.register_blueprint(update_product_bp, url_prefix='/product')
    app.register_blueprint(delete_product_bp, url_prefix='/product')

    return app


