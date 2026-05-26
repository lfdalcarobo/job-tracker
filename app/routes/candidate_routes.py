from flask import Blueprint, request, jsonify
from app.database import get_connection


candidate_routes = Blueprint("candidate_routes", __name__)


# CREATE - create candidate
@candidate_routes.route("/candidate", methods=["POST"])
def create_candidate():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO candidate ( NAME,
                                    DATE_BIRTH,
                                    GENDER,
                                    PHONE,
                                    EMAIL,
                                    ADDRESS,
                                    LINKEDIN)
            VALUES (%s, %s, %s, %s, %s, %s, %s) 
            """

    values = (data.get("name"),
              data.get("date_birth"),
              data.get("gender"),
              data.get("phone"),
              data.get("email"),
              data.get("address"),
              data.get("linkedin"),)

    cursor.execute(query, values)
    connection.commit()

    candidate_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Candidate created", "id": candidate_id}), 201


# READ - get all
@candidate_routes.route("/candidate", methods=["GET"])
def get_all_candidates():
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
            LINKEDIN,
            SITUATION,
            CREATED_AT,
            UPDATED_AT
        FROM candidate
    """)

    candidate = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(candidate)


# READ - by ID
@candidate_routes.route("/candidate/<int:candidate_id>", methods=["GET"])
def get_candidate_by_id(candidate_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM candidate WHERE ID = %s
    """, (candidate_id,))

    candidate = cursor.fetchone()

    cursor.close()
    connection.close()

    if candidate:
        return jsonify(candidate)

    return jsonify({"message": "candidate not found"}), 404


# UPDATE - update candidate
@candidate_routes.route("/candidate/<int:candidate_id>", methods=["PUT"])
def update_candidate(candidate_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE candidate
        SET NAME = %s,
            DATE_BIRTH = %s,
            GENDER = %s,
            PHONE = %s,
            EMAIL = %s,
            ADDRESS = %s,
            LINKEDIN = %s,
            SITUATION = %s
        WHERE ID = %s
    """

    values = (
        data.get("name"),
        data.get("date_birth"),
        data.get("gender"),
        data.get("phone"),
        data.get("email"),
        data.get("address"),
        data.get("linkedin"),
        data.get("situation"),
        candidate_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Candidate updated"})