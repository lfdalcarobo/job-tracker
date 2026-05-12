from database import get_connection

# Conexão com a database

try:
    connection = get_connection()

    if connection.is_connected():
        print("Conectado ao MySQL com sucesso!")

except Exception as error:
    print("Erro ao conectar:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()