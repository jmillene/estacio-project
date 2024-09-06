from connection.connection import connection

def delete_order(order_id):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
            conn.commit()
            return cursor.rowcount > 0
    finally:
        conn.close()