from connection.connection import connection

def get_all_products():
    conn = connection()  # Obtém a conexão do banco de dados
    cursor = conn.cursor()
    
    try:
        # Executa o comando SQL para buscar todos os produtos
        query = "SELECT * FROM products"
        cursor.execute(query)
        
        # Obtém todos os resultados da consulta
        products = cursor.fetchall()
        
        # Cria uma lista de dicionários com os produtos
        products_list = [
            {
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "price": row[3],
                "stock_quantity": row[4]
            }
            for row in products
        ]
        return products_list
    
    except Exception as error:
        raise Exception(f"Erro ao buscar produtos: {error}")
    
    finally:
        # Fecha o cursor e a conexão
        cursor.close()
        conn.close()
