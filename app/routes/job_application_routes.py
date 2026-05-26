from flask import Blueprint, request, jsonify
from app.database import get_connection


job_application_routes = Blueprint("job_application_routes", __name__)


# CREATE - create job application
@job_application_routes.route("/job_application", methods=["POST"])
def create_job_application():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO job_application (   JOB_ID,
                                            CANDIDATE_ID,
                                            APPLICATION_STATUS_ID)
            VALUES (%s, %s, %s) 
            """

    values = (data.get("job_id"),
              data.get("candidate_id"),
              data.get("application_status_id"),)

    cursor.execute(query, values)
    connection.commit()

    job_application_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "job application created", "id": job_application_id}), 201


# READ - get all
@job_application_routes.route("/job_application", methods=["GET"])
def get_all_jobs_applications():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            JOB_ID,
            CANDIDATE_ID,
            APPLICATION_STATUS_ID,
            SITUATION,
            CREATED_AT,
            UPDATED_AT
        FROM job_application
    """)

    job_application = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(job_application)


# READ - by ID
@job_application_routes.route("/job_application/<int:job_application_id>", methods=["GET"])
def get_job_application_by_id(job_application_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM job_application WHERE ID = %s
    """, (job_application_id,))

    job_application = cursor.fetchone()

    cursor.close()
    connection.close()

    if job_application:
        return jsonify(job_application)

    return jsonify({"message": "Job application not found"}), 404


# UPDATE - update job_application
@job_application_routes.route("/job_application/<int:job_application_id>", methods=["PUT"])
def update_job_application(job_application_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE job_application
        SET JOB_ID = %s,
            CANDIDATE_ID = %s,
            APPLICATION_STATUS_ID = %s,
            SITUATION = %s
        WHERE ID = %s
    """

    values = (
        data.get("job_id"),
        data.get("candidate_id"),
        data.get("application_status_id"),
        data.get("situation"),
        job_application_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Job application updated"})