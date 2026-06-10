from app.database import get_connection


# Get all types of locations (for dropdown)
def get_all_types_of_locations():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            NAME
        FROM type_location
        ORDER BY NAME
    """)

    types_of_locations = cursor.fetchall()

    cursor.close()
    connection.close()

    return types_of_locations


# Get type of location by ID (opcional, mas útil para view futura)
def get_type_of_location_by_id(type_location_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            NAME
        FROM type_location
        WHERE ID = %s
    """, (type_location_id,))

    type_of_location = cursor.fetchone()

    cursor.close()
    connection.close()

    return type_of_location