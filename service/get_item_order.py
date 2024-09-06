from connection.connection import connection

def get_order_items(order_id):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT oi.product_id, p.name, oi.quantity FROM order_items oi JOIN products p ON oi.product_id = p.id WHERE oi.order_id = %s",
                (order_id,)
            )
            items = cursor.fetchall()
            if items:
                return [{"product_id": item[0], "product_name": item[1], "quantity": item[2]} for item in items], 200
            return {"message": "Nenhum item encontrado para esta ordem"}, 404
    finally:
        conn.close()
