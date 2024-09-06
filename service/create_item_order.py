from connection.connection import connection

def create_order_item(order_id, product_id, quantity):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            # Verifica se o produto existe e tem estoque suficiente
            cursor.execute("SELECT stock_quantity FROM products WHERE id = %s", (product_id,))
            product = cursor.fetchone()

            if not product:
                return {"message": "Produto não encontrado"}

            stock_quantity = product[0]
            if stock_quantity < quantity:
                return {"message": "Estoque insuficiente"}

            # Cria o item na ordem
            cursor.execute(
                "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                (order_id, product_id, quantity)
            )
            
            # Atualiza o estoque do produto
            cursor.execute(
                "UPDATE products SET stock_quantity = stock_quantity - %s WHERE id = %s",
                (quantity, product_id)
            )

            conn.commit()
            return {"message": "Item adicionado à ordem com sucesso"}
    finally:
        conn.close()
