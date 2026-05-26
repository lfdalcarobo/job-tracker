from flask import Blueprint, request, jsonify
from app.database import get_connection


interview_routes = Blueprint("interview_routes", __name__)


# CREATE - create interview
@interview_routes.route("/interview", methods=["POST"])
def create_interview():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO interview (  JOB_APPLICATION_ID,
                                    INTERVIEW_DATE,
                                    STATUS_INTERVIEW_ID)
            VALUES (%s, %s, %s) 
            """

    values = (data.get("job_application_id"),
              data.get("interview_date"),
              data.get("status_interview_id"),)

    cursor.execute(query, values)
    connection.commit()

    interview_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Interview created", "id": interview_id}), 201


# READ - get all
@interview_routes.route("/interview", methods=["GET"])
def get_all_interviews():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            JOB_APPLICATION_ID,
            INTERVIEW_DATE,
            STATUS_INTERVIEW_ID,
            SITUATION,
            CREATED_AT,
            UPDATED_AT
        FROM interview
    """)

    interview = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(interview)


# READ - by ID
@interview_routes.route("/interview/<int:interview_id>", methods=["GET"])
def get_interview_by_id(interview_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM interview WHERE ID = %s
    """, (interview_id,))

    interview = cursor.fetchone()

    cursor.close()
    connection.close()

    if interview:
        return jsonify(interview)

    return jsonify({"message": "Job application not found"}), 404


# UPDATE - update interview
@interview_routes.route("/interview/<int:interview_id>", methods=["PUT"])
def update_interview(interview_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE interview
        SET JOB_APPLICATION_ID = %s,
            INTERVIEW_DATE = %s,
            STATUS_INTERVIEW_ID = %s,
            SITUATION = %s
        WHERE ID = %s
    """

    values = (
        data.get("job_application_id"),
        data.get("interview_date"),
        data.get("status_interview_id"),
        data.get("situation"),
        interview_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Interview updated"})