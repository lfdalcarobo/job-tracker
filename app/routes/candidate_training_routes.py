from flask import Blueprint, request, jsonify
from app.database import get_connection


candidate_training_routes = Blueprint("candidate_training_routes", __name__)


# CREATE - create training
@candidate_training_routes.route("/candidate_training", methods=["POST"])
def create_candidate_training():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO candidate_training (    CANDIDATE_ID,
                                                DESCRIPTION,
                                                TRAINING_TYPE_ID,
                                                DATE_START,
                                                DATE_END)                                             
            VALUES (%s, %s, %s, %s, %s) 
            """

    values = (data.get("candidate_id"),
              data.get("description"),
              data.get("training_type_id"),
              data.get("date_start"),
              data.get("date_end"),)

    cursor.execute(query, values)
    connection.commit()

    candidate_training_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Training created", "id": candidate_training_id}), 201


# READ - by ID candidate
@candidate_training_routes.route("/candidates/<int:candidate_id>/trainings",methods=["GET"])
def get_candidate_trainings(candidate_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM candidate_training WHERE CANDIDATE_ID = %s
    """, (candidate_id,))

    trainings = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(trainings)

# UPDATE - update training
@candidate_training_routes.route("/candidate_training/<int:candidate_training_id>", methods=["PUT"])
def update_candidate_training(candidate_training_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE candidate_training
        SET DESCRIPTION = %s,
            TRAINING_TYPE_ID = %s,
            DATE_START = %s,
            DATE_END = %s
        WHERE ID = %s
    """

    values = (
        data.get("description"),
        data.get("training_type_id"),
        data.get("date_start"),
        data.get("date_end"),
        candidate_training_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Training updated"})


# DELETE - Delete training
@candidate_training_routes.route("/candidate-training/<int:candidate_training_id>",methods=["DELETE"])
def delete_candidate_training(candidate_training_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM candidate_training
        WHERE ID = %s
    """, (candidate_training_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Training deleted"})