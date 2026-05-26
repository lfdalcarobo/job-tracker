from flask import Blueprint, request, jsonify
from app.database import get_connection

candidate_experience_routes = Blueprint("candidate_experience_routes", __name__)


# CREATE - create experience
@candidate_experience_routes.route("/candidate_experience", methods=["POST"])
def create_candidate_experience():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO candidate_experience (  CANDIDATE_ID,
                                                ENTERPRISE,
                                                POSITION,
                                                DATE_START,
                                                DATE_END,
                                                DESCRIPTION)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

    values = (data.get("candidate_id"),
              data.get("enterprise"),
              data.get("position"),
              data.get("date_start"),
              data.get("date_end"),
              data.get("description"),)

    cursor.execute(query, values)
    connection.commit()

    candidate_experience_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Experience created", "id": candidate_experience_id}), 201


# READ - by ID candidate
@candidate_experience_routes.route("/candidates/<int:candidate_id>/experiences",methods=["GET"])
def get_candidate_experiences(candidate_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM candidate_experience WHERE CANDIDATE_ID = %s
    """, (candidate_id,))

    experiences = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(experiences)


# UPDATE - update experience
@candidate_experience_routes.route("/candidate_experience/<int:candidate_experience_id>", methods=["PUT"])
def update_candidate_experience(candidate_experience_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            UPDATE candidate_experience
            SET ENTERPRISE = %s,
                POSITION = %s,
                DATE_START = %s,
                DATE_END = %s,
                DESCRIPTION = %s
            WHERE ID = %s 
            """

    values = (
        data.get("enterprise"),
        data.get("position"),
        data.get("date_start"),
        data.get("date_end"),
        data.get("description"),
        candidate_experience_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Experience updated"})


# DELETE - Delete experience
@candidate_experience_routes.route("/candidate-experiences/<int:candidate_experience_id>", methods=["DELETE"])
def delete_candidate_experience(candidate_experience_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
                   DELETE
                   FROM candidate_experience
                   WHERE ID = %s
                   """, (candidate_experience_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Experience deleted"})