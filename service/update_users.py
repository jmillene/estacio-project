from connection.connection import connection

def update_user(user_id, name, email, password):
    conn = connection()  # Função que estabelece a conexão com o banco de dados
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE users 
                SET name = %s, email = %s, password = %s 
                WHERE id = %s
                """,
                (name, email, password, user_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                return {"message": "Usuário não encontrado."}
            return {"message": "Usuário atualizado com sucesso"}
    finally:
        conn.close()

