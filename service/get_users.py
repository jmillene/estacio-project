from connection.connection import connection

def list_users(name=None, email=None):
    conn = connection()
    cursor = conn.cursor()
    
    try:
        query = "SELECT * FROM users WHERE TRUE"
        params = []

        if name:
            query += " AND name = %s"
            params.append(name)
        if email:
            query += " AND email = %s"
            params.append(email)

        print(f"Executing query: {query}")
        print(f"With params: {params}")

        cursor.execute(query, tuple(params))
        users = cursor.fetchall()

        print(f"Users fetched: {users}")

        user_list = [
            {
                "id": user[0],
                "name": user[1],
                "email": user[2],
                "password": user[3],
                "created_at": user[4],
                "updated_at": user[5]
            }
            for user in users
        ]
        
        return user_list
    
    except Exception as error:
        raise Exception(f"Erro ao listar usuários: {error}")
    
    finally:
        cursor.close()
        conn.close()
