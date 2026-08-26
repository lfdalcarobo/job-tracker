from app.database import get_connection


# GET ALL LANGUAGES FOR A CANDIDATE
def get_languages_by_candidate(candidate_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT  
            ID as candidate_language_id,
            LANGUAGE_ID as language_id,
            LANGUAGE_NAME(LANGUAGE_ID) as language_name,
            LEVEL_LANGUAGE_ID as level_language_id,
            LEVEL_LANGUAGE_NAME(LEVEL_LANGUAGE_ID) as level_language_name,
            CANDIDATE_ID as candidate_id,
            CREATED_AT as created_at,
            UPDATED_AT as updated_at
        FROM candidate_language
        WHERE CANDIDATE_ID = %s
        ORDER BY ID;
    """, (candidate_id,))

    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result


# GET CANDIDATE_LANGUAGE RECORD BY ITS PRIMARY KEY
def get_candidate_language_by_id(candidate_language_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT  
            ID as candidate_language_id,
            LANGUAGE_ID as language_id,
            LANGUAGE_NAME(LANGUAGE_ID) as language_name,
            LEVEL_LANGUAGE_ID as level_language_id,
            LEVEL_LANGUAGE_NAME(LEVEL_LANGUAGE_ID) as level_language_name,
            CANDIDATE_ID as candidate_id,
            CREATED_AT as created_at,
            UPDATED_AT as updated_at
        FROM candidate_language
        WHERE ID = %s
    """, (candidate_language_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


# INSERT LANGUAGE FOR CANDIDATE
def insert_language(candidate_id, language_id, level_language_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO candidate_language (CANDIDATE_ID, LANGUAGE_ID, LEVEL_LANGUAGE_ID)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE LEVEL_LANGUAGE_ID = VALUES(LEVEL_LANGUAGE_ID);
    """, (candidate_id, language_id, level_language_id))

    connection.commit()
    cursor.close()
    connection.close()


# DELETE CANDIDATE_LANGUAGE RECORD
def delete_language(candidate_language_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM candidate_language
        WHERE ID = %s
    """, (candidate_language_id,))

    connection.commit()
    cursor.close()
    connection.close()


# UPDATE CANDIDATE_LANGUAGE RECORD
def update_language(
    candidate_language_id,
    candidate_id,
    language_id,
    level_language_id
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE candidate_language
        SET
            CANDIDATE_ID = %s,
            LANGUAGE_ID = %s,
            LEVEL_LANGUAGE_ID = %s
        WHERE ID = %s
    """, (
        candidate_id,
        language_id,
        level_language_id,
        candidate_language_id
    ))

    connection.commit()
    cursor.close()
    connection.close()