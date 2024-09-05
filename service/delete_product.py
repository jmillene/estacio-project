from connection.connection import connection

def delete_product(product_id):
    conn = connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao deletar produto: {e}")  # Log de depuração
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
