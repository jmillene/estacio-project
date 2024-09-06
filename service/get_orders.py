from connection.connection import connection

def get_order(order_id):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
            order = cursor.fetchone()
            if order:
                return {
                    "id": order[0],
                    "user_id": order[1],
                    "status": order[2],
                    "created_at": order[3]
                }
            return None
    finally:
        conn.close()