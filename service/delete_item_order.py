from connection.connection import connection

def delete_order_item(order_id, product_id):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            # Verifica se o item existe na ordem
            cursor.execute(
                "SELECT * FROM order_items WHERE order_id = %s AND product_id = %s", 
                (order_id, product_id)
            )
            item = cursor.fetchone()
            
            if not item:
                return False  # Item não encontrado
            
            # Remove o item da ordem
            cursor.execute(
                "DELETE FROM order_items WHERE order_id = %s AND product_id = %s", 
                (order_id, product_id)
            )
            conn.commit()
            return True
    finally:
        conn.close()
