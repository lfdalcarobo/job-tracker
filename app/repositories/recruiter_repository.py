from app.database import get_connection


def get_all_recruiters(name=None, email=None, phone=None, situation=None, enterprise_id=None):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT 
            A.ID as id,
            A.NAME as name,
            A.EMAIL as email,
            A.PHONE as phone,
            A.TYPE_RECRUITER_ID as type_recruiter_id,
            B.DESCRIPTION as type_recruiter_name,
            A.ENTERPRISE_ID as enterprise_id,
            C.NAME as enterprise_name,
            A.SITUATION as situation,
            A.CREATED_AT as created_at,
            A.UPDATED_AT as updated_at
        FROM RECRUITER A
        JOIN TYPE_RECRUITER B ON A.TYPE_RECRUITER_ID = B.ID
        JOIN ENTERPRISE C ON A.ENTERPRISE_ID = C.ID
        WHERE 1=1
    """
    params = []

    if name:
        query += " AND A.NAME LIKE %s"
        params.append(f"%{name}%")

    if email:
        query += " AND A.EMAIL LIKE %s"
        params.append(f"%{email}%")

    if phone:
        query += " AND A.PHONE LIKE %s"
        params.append(f"%{phone}%")

    if situation:
        query += " AND A.SITUATION = %s"
        params.append(situation)

    if enterprise_id:
        query += " AND A.ENTERPRISE_ID = %s"
        params.append(enterprise_id)

    query += " ORDER BY A.NAME"

    cursor.execute(query, tuple(params))
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result


def get_recruiter_by_id(recruiter_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            A.ID as id,
            A.NAME as name,
            A.EMAIL as email,
            A.PHONE as phone,
            A.TYPE_RECRUITER_ID as type_recruiter_id,
            B.DESCRIPTION as type_recruiter_name,
            A.ENTERPRISE_ID as enterprise_id,
            C.NAME as enterprise_name,
            A.SITUATION as situation
        FROM RECRUITER A
        JOIN TYPE_RECRUITER B ON A.TYPE_RECRUITER_ID = B.ID
        JOIN ENTERPRISE C ON A.ENTERPRISE_ID = C.ID
        WHERE A.ID = %s
    """, (recruiter_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    return result


def insert_recruiter(name, email, phone, type_recruiter_id, enterprise_id, situation='A'):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO recruiter (NAME, EMAIL, PHONE, TYPE_RECRUITER_ID, ENTERPRISE_ID, SITUATION)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, email, phone, type_recruiter_id, enterprise_id, situation))

    connection.commit()
    cursor.close()
    connection.close()


def update_recruiter(recruiter_id, name, email, phone, type_recruiter_id, enterprise_id, situation):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE recruiter
        SET
            NAME = %s,
            EMAIL = %s,
            PHONE = %s,
            TYPE_RECRUITER_ID = %s,
            ENTERPRISE_ID = %s,
            SITUATION = %s
        WHERE ID = %s
    """, (name, email, phone, type_recruiter_id, enterprise_id, situation, recruiter_id))

    connection.commit()
    cursor.close()
    connection.close()