from app.database import get_connection


# Get all skills
def get_all_skills():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID as id,
            DESCRIPTION as name
        FROM skill
        WHERE SITUATION = 'A'
        ORDER BY DESCRIPTION
    """)

    skills = cursor.fetchall()

    cursor.close()
    connection.close()

    return skills


# Get skill by ID
def get_skill_by_id(skill_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID as id,
            DESCRIPTION as name
        FROM skill
        WHERE ID = %s
    """, (skill_id,))

    skill = cursor.fetchone()

    cursor.close()
    connection.close()

    return skill