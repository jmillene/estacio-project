from connection.connection import connection

def update_product(product_id, name, description, price, stock_quantity):
    conn = connection()  # Função que estabelece a conexão com o banco de dados
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE products 
                SET name = %s, description = %s, price = %s, stock_quantity = %s 
                WHERE id = %s
                """,
                (name, description, price, stock_quantity, product_id)
            )
            conn.commit()

            # Verificando se algum registro foi atualizado
            if cursor.rowcount == 0:
                return {"message": "Produto não encontrado."}

            return {"message": "Produto atualizado com sucesso"}

    except Exception as e:
        # Captura e registra a exceção
        return {"message": "Erro durante a atualização do produto", "error": str(e)}

    finally:
        conn.close()
