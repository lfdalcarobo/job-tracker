from flask import Blueprint, request, jsonify
from app.database import get_connection

candidate_language_routes = Blueprint("candidate_language_routes", __name__)


# CREATE - create skill candidate
@candidate_language_routes.route("/candidate_language", methods=["POST"])
def create_candidate_language():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO candidate_language (    CANDIDATE_ID,
                                                LANGUAGE_ID,
                                                LEVEL_LANGUAGE_ID)
            VALUES (%s, %s, %s)
            """

    values = (data.get("candidate_id"),
              data.get("language_id"),
              data.get("level_language_id"),)

    cursor.execute(query, values)
    connection.commit()

    candidate_language_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Language linked to the candidate", "id": candidate_language_id}), 201


# READ - by ID candidate
@candidate_language_routes.route("/candidates/<int:candidate_id>/languages",methods=["GET"])
def get_candidate_languages(candidate_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM candidate_language WHERE CANDIDATE_ID = %s
    """, (candidate_id,))

    languages = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(languages)


# UPDATE - update experience
@candidate_language_routes.route("/candidate_language/<int:candidate_language_id>", methods=["PUT"])
def update_candidate_language(candidate_language_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            UPDATE candidate_language
            SET LANGUAGE_ID = %s,
                LEVEL_LANGUAGE_ID = %s
            WHERE ID = %s 
            """

    values = (
        data.get("language_id"),
        data.get("level_language_id"),
        candidate_language_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Language updated"})


# DELETE - Delete experience
@candidate_language_routes.route("/candidate-languages/<int:candidate_language_id>", methods=["DELETE"])
def delete_candidate_language(candidate_language_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
                   DELETE
                   FROM candidate_language
                   WHERE ID = %s
                   """, (candidate_language_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Language deleted"})