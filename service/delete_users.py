from connection.connection import connection

def delete_user(user_id):
    conn = connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")  # Log de depuração
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
