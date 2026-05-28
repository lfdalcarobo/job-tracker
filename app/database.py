import mysql.connector
import os
from mysql.connector import Error

def get_connection():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "sysadmin"),
            password=os.getenv("DB_PASSWORD", "0000"),
            database=os.getenv("DB_NAME", "job_tracker")
        )
    except Error as e:
        print(f"Erro ao conectar no MySQL: {e}")
        return None