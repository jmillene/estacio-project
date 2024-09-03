from connection.connection import connection

def create_users(name, email,password):
    conn = connection()  # Obtém a conexão do banco de dados
    cursor = conn.cursor()
    
    try:
        # Executa o comando SQL para inserir o usuário
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        
        # Confirma a transação
        conn.commit()
        
    except Exception as error:
        # Lança a exceção para que o controlador possa tratá-la
        raise Exception(f"Erro ao adicionar usuário: {error}")
    
    finally:
        # Fecha o cursor e a conexão
        cursor.close()
        conn.close()
