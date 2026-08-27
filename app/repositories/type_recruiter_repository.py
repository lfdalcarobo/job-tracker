from app.database import get_connection


def get_all_type_recruiters():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            ID as id,
            DESCRIPTION as description
        FROM TYPE_RECRUITER
        WHERE SITUATION = 'A'
        ORDER BY DESCRIPTION
    """)
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result