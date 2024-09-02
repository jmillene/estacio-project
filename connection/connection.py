import psycopg2

def connection():
    try:
        conn = psycopg2.connect(
            user="user",
            password="password",
            host="db",
            port="5432",
            database="estacio_project"
        )
        cursor = conn.cursor()
        print("Conexão com PostgreSQL realizada com sucesso!")
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Erro ao conectar ao PostgreSQL: {error}")
