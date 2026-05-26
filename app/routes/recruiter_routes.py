from flask import Blueprint, request, jsonify
from app.database import get_connection


recruiter_routes = Blueprint("recruiter_routes", __name__)


# CREATE - create recruiter
@recruiter_routes.route("/recruiter", methods=["POST"])
def create_recruiter():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO recruiter ( NAME,
                                    TYPE_RECRUITER_ID)
            VALUES (%s, %s) 
            """

    values = (data.get("name"),data.get("type_recruiter_id"))

    cursor.execute(query, values)
    connection.commit()

    recruiter_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Recruiter created", "id": recruiter_id}), 201


# READ - get all
@recruiter_routes.route("/recruiter", methods=["GET"])
def get_all_recruiters():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            NAME,
            TYPE_RECRUITER_ID,
            SITUATION,
            CREATED_AT,
            UPDATED_AT
        FROM recruiter
    """)

    recruiter = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(recruiter)


# READ - by ID
@recruiter_routes.route("/recruiter/<int:recruiter_id>", methods=["GET"])
def get_recruiter_by_id(recruiter_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM recruiter WHERE ID = %s
    """, (recruiter_id,))

    recruiter = cursor.fetchone()

    cursor.close()
    connection.close()

    if recruiter:
        return jsonify(recruiter)

    return jsonify({"message": "Recruiter not found"}), 404


# UPDATE - updating recruiter
@recruiter_routes.route("/recruiter/<int:recruiter_id>", methods=["PUT"])
def update_recruiter(recruiter_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE recruiter
        SET NAME = %s,
            TYPE_RECRUITER_ID = %s,
            SITUATION = %s
        WHERE ID = %s
    """

    values = (
        data.get("name"),
        data.get("type_recruiter_id"),
        data.get("situation"),
        recruiter_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Recruiter updated"})