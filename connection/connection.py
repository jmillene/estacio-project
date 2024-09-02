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
        print("Conexão com PostgreSQL realizada com sucesso!")
        return conn  # Retorna a conexão para uso posterior
    except Exception as error:
        print(f"Erro ao conectar ao PostgreSQL: {error}")
        raise  # Re-raise o erro para que possa ser tratado onde a função é chamada
