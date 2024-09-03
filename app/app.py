from flask import Flask
from routes.create_users import user_bp
from routes.list_users import user_bp
from dotenv import load_dotenv
import os

def create_app():
    # Carrega variáveis do arquivo .env
    load_dotenv()
    
    app = Flask(__name__)

    # Registra o blueprint para as rotas de usuário
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
