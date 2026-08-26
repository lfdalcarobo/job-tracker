from app.database import get_connection


# Get all languages
def get_all_languages():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID as id,
            DESCRIPTION as name
        FROM language
        ORDER BY DESCRIPTION
    """)

    languages = cursor.fetchall()

    cursor.close()
    connection.close()

    return languages


# Get language by ID
def get_language_by_id(language_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID as id,
            DESCRIPTION as name
        FROM language
        WHERE ID = %s
    """, (language_id,))

    language = cursor.fetchone()

    cursor.close()
    connection.close()

    return language