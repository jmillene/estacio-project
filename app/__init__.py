from flask import Flask

app = Flask(__name__)

from . import routes  # Importa o módulo de rotas depois que o `app` é criado
