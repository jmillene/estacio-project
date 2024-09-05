from connection.connection import connection

def create_product(name, description, price, stock_quantity):
    conn = connection()  # Obtém a conexão do banco de dados
    cursor = conn.cursor()
    
    try:
        # Executa o comando SQL para inserir o produto
        query = """
        INSERT INTO products (name, description, price, stock_quantity)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, description, price, stock_quantity))
        
        # Confirma a transação
        conn.commit()
        
    except Exception as error:
        # Lança a exceção para que o controlador possa tratá-la
        raise Exception(f"Erro ao adicionar produto: {error}")
    
    finally:
        # Fecha o cursor e a conexão
        cursor.close()
        conn.close()
