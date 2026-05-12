import mysql.connector

# credenciais de acesso para conexão com a database

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="sysadmin",
        password="0000",
        database="job_tracker"
    )

    return connection