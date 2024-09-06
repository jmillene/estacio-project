from connection.connection import connection
from datetime import datetime

def create_order(user_id):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            total = 0.0 

            cursor.execute(
                "INSERT INTO orders (user_id, status, total) VALUES (%s, %s, %s) RETURNING id", 
                (user_id, 'pending', total)
            )
            order_id = cursor.fetchone()[0]
            conn.commit()
            return {"message": "Ordem criada com sucesso", "order_id": order_id}
    finally:
        conn.close()
