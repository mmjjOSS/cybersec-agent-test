import sqlite3

def buscar_usuario(username):
    # Codigo propositalmente vulneravel para testar os agentes.
    # Usa concatenacao direta em vez de consultas parametrizadas.
    query = f"SELECT * FROM usuarios WHERE username = '{username}'"
    
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

print(buscar_usuario("admin"))
