from flask import Flask
from routes.create_users import create_user_bp
from routes.get_users import list_users_bp
from routes.update_users import update_user_bp
from routes.delete_users import delete_user_bp 
from routes.create_product import create_product_bp
from routes.get_product import list_products_bp
from routes.update_products import update_product_bp
from routes.delete_product import delete_product_bp
from routes.create_order import create_order_bp
from routes.get_order import list_orders_bp
from routes.update_order import update_order_bp
from routes.delete_order import delete_order_bp
from routes.create_order_item import create_order_item_bp
from routes.get_item_order import list_item_orders_bp
from routes.update_item_order import update_order_items_bp
from routes.delete_item_order import delete_order_items_bp

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
    app.register_blueprint(create_order_bp, url_prefix='/order')
    app.register_blueprint(list_orders_bp, url_prefix='/order')
    app.register_blueprint(update_order_bp, url_prefix='/order')
    app.register_blueprint(delete_order_bp, url_prefix='/order')
    app.register_blueprint(create_order_item_bp, url_prefix='/item_order')
    app.register_blueprint(list_item_orders_bp, url_prefix='/item_order')
    app.register_blueprint(update_order_items_bp, url_prefix='/item_order')
    app.register_blueprint(delete_order_items_bp, url_prefix='/item_order')

    return app
