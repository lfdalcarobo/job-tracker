from flask import Blueprint, request, jsonify
from app.database import get_connection

job_routes = Blueprint("job_routes", __name__)


# CREATE - criar job

@job_routes.route("/job", methods=["POST"])
def create_job():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO job (POSITION,
                             DESCRIPTION,
                             DATE_OPENING,
                             DATE_CLOSING,
                             ENTERPRISE_ID)
            VALUES (%s, %s, %s, %s, %s)
            """

    values = (
        data.get("position"),
        data.get("description"),
        data.get("date_opening"),
        data.get("date_closing"),
        data.get("enterprise_id")
    )

    cursor.execute(query, values)
    connection.commit()

    job_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Job created", "id": job_id}), 201



# READ - listar todos
@job_routes.route("/job", methods=["GET"])
def get_jobs():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ID,
            POSITION,
            DESCRIPTION,
            DATE_OPENING,
            DATE_CLOSING,
            ENTERPRISE_ID,
            SITUATION,
            CREATED_AT,
            UPDATED_AT
        FROM job
    """)

    jobs = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(jobs)


# READ - por ID
@job_routes.route("/job/<int:job_id>", methods=["GET"])
def get_job(job_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM job WHERE ID = %s
    """, (job_id,))

    job = cursor.fetchone()

    cursor.close()
    connection.close()

    if job:
        return jsonify(job)

    return jsonify({"message": "Job not found"}), 404


# UPDATE - atualizar job
@job_routes.route("/job/<int:job_id>", methods=["PUT"])
def update_job(job_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE job
        SET POSITION = %s,
            DESCRIPTION = %s,
            DATE_OPENING = %s,
            DATE_CLOSING = %s,
            ENTERPRISE_ID = %s,
            SITUATION = %S
        WHERE ID = %s
    """

    values = (
        data.get("position"),
        data.get("description"),
        data.get("date_opening"),
        data.get("date_closing"),
        data.get("enterprise_id"),
        data.get("situation"),
        job_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Job updated"})