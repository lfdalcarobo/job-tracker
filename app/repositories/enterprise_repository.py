from app.database import get_connection


# Get all enterprises
def get_all_enterprises():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            NAME,
            SITUATION,
            CREATED_AT,
            UPDATED_AT
        FROM enterprise
    """)

    enterprises = cursor.fetchall()

    cursor.close()
    connection.close()

    return enterprises


# Create enterprise
def create_enterprise_db(name,situation):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO enterprise (NAME,SITUATION)
            VALUES (%s, %s) 
    """, (name,situation))

    connection.commit()

    cursor.close()
    connection.close()


# Update enterprise
def update_enterprise_db(id, name, situation):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE enterprise
        SET name = %s, situation = %s
        WHERE id = %s
    """, (name, situation, id))

    connection.commit()

    cursor.close()
    connection.close()


# View enterprise by ID
def get_enterprise_by_id(id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT name, situation
        FROM enterprise
        WHERE id = %s
    """, (id,))

    enterprise = cursor.fetchone()

    cursor.close()
    connection.close()

    return enterprise