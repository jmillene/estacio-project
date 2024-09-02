from . import app  # Importa o `app` do módulo `app`
from controller.user import create_user

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/createuser', methods=['POST'])
def add_user():
    return create_user()
