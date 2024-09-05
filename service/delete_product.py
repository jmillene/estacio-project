from connection.connection import connection

def delete_product(product_id):
    conn = connection()  # Estabelece a conexão com o banco de dados
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            return {"message": "Product deleted successfully"}
        else:
            return {"message": "Product not found"}
    
    except Exception as e:
        print(f"Erro ao deletar produto: {e}")  # Log de depuração
        conn.rollback()
        return {"message": f"Erro ao deletar produto: {e}"}
    
    finally:
        cursor.close()
        conn.close()
