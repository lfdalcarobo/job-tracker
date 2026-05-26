from flask import Blueprint, request, jsonify
from app.database import get_connection


enterprise_routes = Blueprint("enterprise_routes", __name__)


# CREATE - create enterprise
@enterprise_routes.route("/enterprise", methods=["POST"])
def create_enterprise():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO enterprise (NAME)
            VALUES (%s) 
            """

    values = (data.get("name"),)

    cursor.execute(query, values)
    connection.commit()

    enterprise_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Enterprise created", "id": enterprise_id}), 201


# READ - get all
@enterprise_routes.route("/enterprise", methods=["GET"])
def get_all_enterprises():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            NAME,
            SITUATION,
            CREATED_AT,
            UPDATED_AT
        FROM enterprise
    """)

    enterprise = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(enterprise)


# READ - by ID
@enterprise_routes.route("/enterprise/<int:enterprise_id>", methods=["GET"])
def get_enterprise_by_id(enterprise_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM enterprise WHERE ID = %s
    """, (enterprise_id,))

    enterprise = cursor.fetchone()

    cursor.close()
    connection.close()

    if enterprise:
        return jsonify(enterprise)

    return jsonify({"message": "Enterprise not found"}), 404


# UPDATE - update enterprise
@enterprise_routes.route("/enterprise/<int:enterprise_id>", methods=["PUT"])
def update_enterprise(enterprise_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE enterprise
        SET NAME = %s,
            SITUATION = %s
        WHERE ID = %s
    """

    values = (
        data.get("name"),
        data.get("situation"),
        enterprise_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Enterprise updated"})