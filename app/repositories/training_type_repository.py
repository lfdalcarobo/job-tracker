from app.database import get_connection


# Get all training types
def get_all_training_types():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID as id,
            DESCRIPTION as name
        FROM training_type
        ORDER BY DESCRIPTION
    """)

    training_types = cursor.fetchall()

    cursor.close()
    connection.close()

    return training_types


# Get training type by ID
def get_training_type_by_id(training_type_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID as id,
            DESCRIPTION as name
        FROM training_type
        WHERE ID = %s
    """, (training_type_id,))

    training_type = cursor.fetchone()

    cursor.close()
    connection.close()

    return training_type