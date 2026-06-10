from app.database import get_connection


# Get all countries (for dropdown)
def get_all_countries():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            NAME
        FROM country
        ORDER BY NAME
    """)

    countries = cursor.fetchall()

    cursor.close()
    connection.close()

    return countries


# Get country by ID (opcional, mas útil para view futura)
def get_country_by_id(country_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            NAME
        FROM country
        WHERE ID = %s
    """, (country_id,))

    country = cursor.fetchone()

    cursor.close()
    connection.close()

    return country