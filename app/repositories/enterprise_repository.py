from app.database import get_connection


# Get all enterprises
def get_all_enterprises(name=None, situation=None):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    sql = """
        SELECT ID, NAME, SITUATION, CREATED_AT, UPDATED_AT
        FROM enterprise
        WHERE 1=1
        
    """

    params = []

    if name:
        sql += " AND NAME LIKE %s"
        params.append(f"%{name}%")


    # ✔ SÓ FILTRA SE NÃO FOR NONE
    if situation:
        sql += " AND SITUATION = %s"
        params.append(situation)


    sql += " ORDER BY NAME ASC"

    cursor.execute(sql, params)

    enterprises = cursor.fetchall()

    cursor.close()
    connection.close()

    return enterprises


# Create enterprise
def create_enterprise_db(name, situation):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO enterprise (
            NAME,
            SITUATION
        )
        VALUES (%s, %s)
    """, (name, situation))

    connection.commit()

    # captura o ID gerado pelo INSERT
    enterprise_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return enterprise_id


# Update enterprise
def update_enterprise_db(id, name, situation):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            UPDATE enterprise
            SET NAME = %s,
                SITUATION = %s
            WHERE ID = %s
        """, (name, situation, id))

        connection.commit()

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()


# View enterprise by ID
def get_enterprise_by_id(id):

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
        WHERE ID = %s
    """, (id,))

    enterprise = cursor.fetchone()

    cursor.close()
    connection.close()

    return enterprise