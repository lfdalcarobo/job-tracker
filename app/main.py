from database import get_connection

# Conexão com a database

try:
    connection = get_connection()

    if connection.is_connected():
        print("Successfully connected to MySQL!")

except Exception as error:
    print("Error connecting:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()