from app.database import get_connection


def get_experiences_by_candidate(candidate_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT 	ID,
		CANDIDATE_ID,
        ENTERPRISE,
        POSITION,
        COUNTRY_ID,
        COUNTRY_NAME(COUNTRY_ID) AS COUNTRY_NAME,
        TYPE_LOCATION_ID,
        TYPE_LOCATION_NAME(TYPE_LOCATION_ID) AS TYPE_LOCATION_NAME,          
        START_DATE,
        END_DATE,
        DESCRIPTION,
        CREATED_AT,
        UPDATED_AT
FROM 	candidate_experience
        WHERE CANDIDATE_ID = %s
        ORDER BY START_DATE DESC
    """, (candidate_id,))

    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result

# GET EXPERIENCE BY ID
def get_experience_by_id(exp_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            CANDIDATE_ID,
            ENTERPRISE,
            POSITION,
            COUNTRY_ID,
            COUNTRY_NAME(COUNTRY_ID) AS COUNTRY_NAME,
            TYPE_LOCATION_ID,
            TYPE_LOCATION_NAME(TYPE_LOCATION_ID) AS TYPE_LOCATION_NAME,
            START_DATE,
            END_DATE,
            DESCRIPTION,
            CREATED_AT,
            UPDATED_AT
        FROM candidate_experience
        WHERE ID = %s
    """, (exp_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

# INSERT EXPERIENCE
def insert_experience(data):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO candidate_experience
        (CANDIDATE_ID, ENTERPRISE, POSITION, COUNTRY_ID, TYPE_LOCATION_ID, START_DATE, END_DATE, DESCRIPTION)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data["candidate_id"],
        data["enterprise"],
        data["position"],
        data["country_id"],
        data["type_location_id"],
        data["start_date"],
        data["end_date"],
        data.get("description")
    ))

    connection.commit()
    cursor.close()
    connection.close()


# DELETE EXPERIENCE
def delete_experience(exp_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM candidate_experience
        WHERE ID = %s
    """, (exp_id,))

    connection.commit()
    cursor.close()
    connection.close()


# UPDATE EXPERIENCE
def update_experience(
    exp_id,
    enterprise,
    position,
    country_id,
    type_location_id,
    start_date,
    end_date,
    description
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE candidate_experience
        SET
            ENTERPRISE = %s,
            POSITION = %s,
            COUNTRY_ID = %s,
            TYPE_LOCATION_ID = %s,
            START_DATE = %s,
            END_DATE = %s,
            DESCRIPTION = %s
        WHERE ID = %s
    """, (
        enterprise,
        position,
        country_id,
        type_location_id,
        start_date,
        end_date,
        description,
        exp_id
    ))

    connection.commit()
    cursor.close()
    connection.close()