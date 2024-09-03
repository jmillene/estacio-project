from flask import Flask
from routes.create_users import create_user_bp
from routes.list_users import list_users_bp
from routes.update_users import update_user_bp
from dotenv import load_dotenv

def create_app():
    # Carrega variáveis do arquivo .env
    load_dotenv()
    
    app = Flask(__name__)

    # Registra os blueprints
    app.register_blueprint(create_user_bp, url_prefix='/user')
    app.register_blueprint(list_users_bp, url_prefix='/user')
    app.register_blueprint(update_user_bp, url_prefix='/user')

    return app
