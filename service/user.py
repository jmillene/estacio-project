from connection.connection import connection

def create_user(name, email):
    conn = connection
    cursor = conn.cursor()
    
    try:
        # Executa o comando SQL para inserir o usuário
        cursor.execute("INSERT INTO user (name, email) VALUES (%s, %s)", (name, email))
        
        # Confirma a transação
        conn.commit()
        
    except Exception as error:
        # Lança a exceção para que o controlador possa tratá-la
        raise Exception(f"Erro ao adicionar usuário: {error}")
    
    finally:
        # Fecha o cursor e a conexão
        cursor.close()
        conn.close()
