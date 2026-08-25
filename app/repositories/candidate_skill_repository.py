from app.database import get_connection


def get_skills_by_candidate(candidate_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT  
            cs.ID as id,
            cs.CANDIDATE_ID as candidate_id,
            cs.SKILL_ID as skill_id,
            s.DESCRIPTION as name,
            cs.CREATED_AT as created_at,
            cs.UPDATED_AT as updated_at
        FROM candidate_skill cs
        JOIN skill s ON cs.SKILL_ID = s.ID
        WHERE cs.CANDIDATE_ID = %s
        ORDER BY s.DESCRIPTION
    """, (candidate_id,))

    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result

# GET SKILL BY ID
def get_skill_by_id(candidate_skill_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            cs.ID as id,
            cs.CANDIDATE_ID,
            cs.SKILL_ID,
            s.DESCRIPTION AS name
        FROM candidate_skill cs
        JOIN skill s ON cs.SKILL_ID = s.ID
        WHERE cs.CANDIDATE_ID = %s
    """, (candidate_skill_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

# INSERT SKILL
def insert_skill(
    candidate_id,
    skill_id
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO candidate_skill
        (
            CANDIDATE_ID,
            SKILL_ID
        )
        VALUES (%s, %s)
    """, (
        candidate_id,
        skill_id

    ))

    connection.commit()
    cursor.close()
    connection.close()


# DELETE SKILL
def delete_skill(candidate_skill_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM candidate_skill
        WHERE ID = %s
    """, (candidate_skill_id,))

    connection.commit()
    cursor.close()
    connection.close()


# UPDATE SKILL
def update_skill(
    candidate_skill_id,
    skill_id
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE candidate_skill
        SET
            SKILL_ID = %s
        WHERE ID = %s
    """, (
        skill_id,
        candidate_skill_id
    ))

    connection.commit()
    cursor.close()
    connection.close()