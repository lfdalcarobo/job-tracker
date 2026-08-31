from app.database import get_connection


def get_all_jobs(position=None, description=None, type_location_id=None, city=None, country_id=None, date_opening=None, date_closing=None, enterprise_id=None, situation=None):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT 
            A.ID as id,
            A.POSITION as position,
            A.DESCRIPTION as description,
            A.TYPE_LOCATION_ID as type_location_id,
            TL.NAME as type_location_name,
            A.CITY as city,
            A.COUNTRY_ID as country_id,
            C.NAME as country_name,
            A.DATE_OPENING as date_opening,
            A.DATE_CLOSING as date_closing,
            A.ENTERPRISE_ID as enterprise_id,
            E.NAME as enterprise_name,
            A.SITUATION as situation,
            A.CREATED_AT as created_at,
            A.UPDATED_AT as updated_at
        FROM JOB A
        LEFT JOIN TYPE_LOCATION TL ON A.TYPE_LOCATION_ID = TL.ID
        LEFT JOIN COUNTRY C ON A.COUNTRY_ID = C.ID
        LEFT JOIN ENTERPRISE E ON A.ENTERPRISE_ID = E.ID
        WHERE 1=1
    """
    params = []

    if position:
        query += " AND A.POSITION LIKE %s"
        params.append(f"%{position}%")

    if description:
        query += " AND A.DESCRIPTION LIKE %s"
        params.append(f"%{description}%")

    if type_location_id:
        query += " AND A.TYPE_LOCATION_ID = %s"
        params.append(type_location_id)

    if city:
        query += " AND A.CITY LIKE %s"
        params.append(f"%{city}%")
    
    if country_id:
        query += " AND A.COUNTRY_ID = %s"
        params.append(country_id)

    if date_opening:
        query += " AND A.DATE_OPENING >= %s"
        params.append(date_opening)
    
    if date_closing:
        query += " AND A.DATE_CLOSING <= %s"
        params.append(date_closing)

    if situation:
        query += " AND A.SITUATION = %s"
        params.append(situation)

    if enterprise_id:
        query += " AND A.ENTERPRISE_ID = %s"
        params.append(enterprise_id)

    query += " ORDER BY A.POSITION"

    cursor.execute(query, tuple(params))
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result


def get_job_by_id(job_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            A.ID as id,
            A.POSITION as position,
            A.DESCRIPTION as description,
            A.TYPE_LOCATION_ID as type_location_id,
            TL.NAME as type_location_name,
            A.CITY as city,
            A.COUNTRY_ID as country_id,
            C.NAME as country_name,
            A.DATE_OPENING as date_opening,
            A.DATE_CLOSING as date_closing,
            A.ENTERPRISE_ID as enterprise_id,
            E.NAME as enterprise_name,
            A.SITUATION as situation,
            A.CREATED_AT as created_at,
            A.UPDATED_AT as updated_at
        FROM JOB A
        LEFT JOIN TYPE_LOCATION TL ON A.TYPE_LOCATION_ID = TL.ID
        LEFT JOIN COUNTRY C ON A.COUNTRY_ID = C.ID
        LEFT JOIN ENTERPRISE E ON A.ENTERPRISE_ID = E.ID
        WHERE A.ID = %s
    """, (job_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    return result


def insert_job(position, description, type_location_id, city, country_id, date_opening, date_closing, enterprise_id, situation='A'):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO job (POSITION, DESCRIPTION, TYPE_LOCATION_ID, CITY, COUNTRY_ID, DATE_OPENING, DATE_CLOSING, ENTERPRISE_ID, SITUATION)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (position, description, type_location_id, city, country_id, date_opening, date_closing, enterprise_id, situation))

    connection.commit()
    cursor.close()
    connection.close()


def update_job(job_id, position, description, type_location_id, city, country_id, date_opening, date_closing, enterprise_id, situation):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE job
        SET
            POSITION = %s,
            DESCRIPTION = %s,
            TYPE_LOCATION_ID = %s,
            CITY = %s,
            COUNTRY_ID = %s,
            DATE_OPENING = %s,
            DATE_CLOSING = %s,
            ENTERPRISE_ID = %s,
            SITUATION = %s
        WHERE ID = %s
    """, (position, description, type_location_id, city, country_id, date_opening, date_closing, enterprise_id, situation, job_id))

    connection.commit()
    cursor.close()
    connection.close()