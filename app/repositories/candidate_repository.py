from app.database import get_connection


# Get all candidates
def get_all_candidates(name=None, gender=None, email=None, phone=None, date_birth=None):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    sql = """
        SELECT
            ID,
            NAME,
            DATE_BIRTH,
            GENDER,
            PHONE,
            EMAIL,
            ADDRESS,
            CITY,
            COUNTRY_NAME(COUNTRY) AS COUNTRY_NAME,
            LINKEDIN,
            CREATED_AT,
            UPDATED_AT
        FROM
            CANDIDATE
        WHERE 1=1
        
    """

    params = []

    if name:
        sql += " AND NAME LIKE %s"
        params.append(f"%{name}%")


    # ✔ SÓ FILTRA SE NÃO FOR NONE
    if gender:
        sql += " AND GENDER = %s"
        params.append(gender)
    if email:
        sql += " AND EMAIL LIKE %s"
        params.append(f"%{email}%")
    if phone:
        sql += " AND PHONE = %s"
        params.append(phone)
    if date_birth:
        sql += " AND DATE_BIRTH = %s"
        params.append(date_birth)


    sql += " ORDER BY NAME ASC"

    cursor.execute(sql, params)

    candidates = cursor.fetchall()

    cursor.close()
    connection.close()

    return candidates


# Create candidate
def create_candidate_db(name, date_birth, gender, phone, email, address, city, country, linkedin):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO CANDIDATE (
                    NAME,
                    DATE_BIRTH,
                    GENDER,
                    PHONE,
                    EMAIL,
                    ADDRESS,
                    CITY,
                    COUNTRY,
                    LINKEDIN)
        VALUES (CAPFIRST(%s), %s, %s, %s, LOWER(%s), CAPFIRST(%s), CAPFIRST(%s), %s, %s)
    """, (name, date_birth, gender, phone, email, address, city, country, linkedin))

    connection.commit()

    # captura o ID gerado pelo INSERT
    candidate_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return candidate_id


# Update candidate
def update_candidate_db(id, name, date_birth, gender, phone, email, address, city, country, linkedin):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            UPDATE CANDIDATE
            SET NAME = CAPFIRST(%s),
                DATE_BIRTH = %s,
                GENDER = %s,
                PHONE = %s,
                EMAIL = LOWER(%s),
                ADDRESS = CAPFIRST(%s),
                CITY = CAPFIRST(%s),
                COUNTRY = %s,
                LINKEDIN = %s
            WHERE ID = %s
        """, (name, date_birth, gender, phone, email, address, city, country, linkedin, id))

        connection.commit()

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()


# View candidate by ID
def get_candidate_by_id(id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            NAME,
            DATE_BIRTH,
            GENDER,
            PHONE,
            EMAIL,
            ADDRESS,
            CITY,
            COUNTRY,   
            COUNTRY_NAME(COUNTRY) AS COUNTRY_NAME,
            LINKEDIN,
            CREATED_AT,
            UPDATED_AT
        FROM CANDIDATE
        WHERE ID = %s
    """, (id,))

    candidate = cursor.fetchone()

    cursor.close()
    connection.close()

    return candidate