from flask import Flask
from connection.connection import connection

app = Flask(__name__)

@app.route('/')
def hello():
    connection()  # Testa a conexão ao acessar a rota principal
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Mantém o servidor rodando
