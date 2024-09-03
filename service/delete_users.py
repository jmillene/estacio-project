import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connection.connection import connection

def delete_user(user_id):
    conn = connection()
    cursor = conn.cursor()

    try:
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()

        return {"message": "Usuário excluído com sucesso."}
    
    except Exception as error:
        conn.rollback()
        raise Exception(f"Erro ao excluir usuário: {error}")
    
    finally:
        cursor.close()
        conn.close()
