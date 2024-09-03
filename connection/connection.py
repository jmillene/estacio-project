import os
import psycopg2
from dotenv import load_dotenv

def connection():
    load_dotenv()
    try:
        conn = psycopg2.connect(
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT"),
            database=os.getenv("DATABASE_NAME")
        )
        print("Conexão com PostgreSQL realizada com sucesso!")
        return conn
    except Exception as error:
        print(f"Erro ao conectar ao PostgreSQL: {error}")
        raise
