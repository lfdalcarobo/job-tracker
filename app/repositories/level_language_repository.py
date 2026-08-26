from app.database import get_connection


# Get all level languages
def get_all_level_languages():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID as id,
            DESCRIPTION as name
        FROM level_language
        ORDER BY DESCRIPTION
    """)

    languages = cursor.fetchall()

    cursor.close()
    connection.close()

    return languages


# Get level language by ID
def get_level_language_by_id(level_language_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID as id,
            DESCRIPTION as name
        FROM level_language
        WHERE ID = %s
    """, (level_language_id,))

    level_language = cursor.fetchone()

    cursor.close()
    connection.close()

    return level_language