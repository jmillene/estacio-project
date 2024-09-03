import os
import psycopg2
from dotenv import load_dotenv

def connection():
    load_dotenv()
    try:
        conn = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        print("Conexão com PostgreSQL realizada com sucesso!")
        return conn
    except Exception as error:
        print(f"Erro ao conectar ao PostgreSQL: {error}")
        raise
