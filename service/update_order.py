from connection.connection import connection

def update_order(order_id, status):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE orders SET status = %s WHERE id = %s", (status, order_id))
            conn.commit()
            return cursor.rowcount > 0
    finally:
        conn.close()