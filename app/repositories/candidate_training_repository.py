from app.database import get_connection


def get_trainings_by_candidate(candidate_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT 	
            ID as id,
            CANDIDATE_ID as candidate_id,
            DESCRIPTION as description,
            TRAINING_TYPE_ID as training_type_id,
            TRAINING_TYPE_NAME(TRAINING_TYPE_ID) as training_name,
            COUNTRY_ID as country_id,
            COUNTRY_NAME(COUNTRY_ID) as country_name,
            START_DATE as start_date,
            END_DATE as end_date,
            CREATED_AT as created_at,
            UPDATED_AT as updated_at
        FROM candidate_training
        WHERE CANDIDATE_ID = %s
        ORDER BY START_DATE DESC;
    """, (candidate_id,))

    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result

# GET TRAINING BY ID
def get_training_by_id(training_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID as id,
            CANDIDATE_ID as candidate_id,
            DESCRIPTION as description,
            TRAINING_TYPE_ID as training_type_id,
            COUNTRY_ID as country_id,
            START_DATE as start_date,
            END_DATE as end_date,
            CREATED_AT as created_at,
            UPDATED_AT as updated_at
        FROM candidate_training
        WHERE ID = %s
    """, (training_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

# INSERT TRAINING
def insert_training(
    candidate_id,
    description,
    training_type_id,
    country_id,
    start_date,
    end_date
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO candidate_training
        (
            CANDIDATE_ID,
            DESCRIPTION,
            TRAINING_TYPE_ID,
            COUNTRY_ID,
            START_DATE,
            END_DATE
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        candidate_id,
        description,
        training_type_id,
        country_id,
        start_date,
        end_date
    ))

    connection.commit()
    cursor.close()
    connection.close()


# DELETE TRAINING
def delete_training(training_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM candidate_training
        WHERE ID = %s
    """, (training_id,))

    connection.commit()
    cursor.close()
    connection.close()


# UPDATE TRAINING
def update_training(
    training_id,
    description,
    training_type_id,
    country_id,
    start_date,
    end_date
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE candidate_training
        SET
            DESCRIPTION = %s,
            TRAINING_TYPE_ID = %s,
            COUNTRY_ID = %s,
            START_DATE = %s,
            END_DATE = %s
        WHERE ID = %s
    """, (
        description,
        training_type_id,
        country_id,
        start_date,
        end_date,
        training_id
    ))

    connection.commit()
    cursor.close()
    connection.close()