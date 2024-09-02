from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    # Obtém a porta a partir da variável de ambiente ou usa a padrão
    port = int(os.getenv("API_PORT", 3002))
    
    app.run(host="0.0.0.0", port=port)
