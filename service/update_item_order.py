from connection.connection import connection

def update_order_item(order_id, product_id, quantity):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            # Verifica se o item já existe na ordem
            cursor.execute("SELECT quantity FROM order_items WHERE order_id = %s AND product_id = %s", (order_id, product_id))
            item = cursor.fetchone()

            if not item:
                return {"message": "Item não encontrado na ordem"}

            # Atualiza a quantidade do item
            cursor.execute(
                "UPDATE order_items SET quantity = %s WHERE order_id = %s AND product_id = %s",
                (quantity, order_id, product_id)
            )
            
            # Atualiza o estoque (reverte o estoque anterior e aplica a nova quantidade)
            previous_quantity = item[0]
            cursor.execute(
                "UPDATE products SET stock_quantity = stock_quantity + %s - %s WHERE id = %s",
                (previous_quantity, quantity, product_id)
            )

            conn.commit()
            return {"message": "Item atualizado com sucesso"}
    finally:
        conn.close()
