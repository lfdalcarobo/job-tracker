from flask import Blueprint, request, jsonify
from app.database import get_connection

candidate_skill_routes = Blueprint("candidate_skill_routes", __name__)


# CREATE - create skill candidate
@candidate_skill_routes.route("/candidate_skill", methods=["POST"])
def create_candidate_skill():
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO candidate_skill (   CANDIDATE_ID,
                                            SKILL_ID)
            VALUES (%s, %s, %s)
            """

    values = (data.get("candidate_id"),
              data.get("skill_id"),)

    cursor.execute(query, values)
    connection.commit()

    candidate_skill_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Skill linked to the candidate", "id": candidate_skill_id}), 201


# READ - by ID candidate
@candidate_skill_routes.route("/candidates/<int:candidate_id>/skills",methods=["GET"])
def get_candidate_skills(candidate_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM candidate_skill WHERE CANDIDATE_ID = %s
    """, (candidate_id,))

    skills = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(skills)


# UPDATE - update experience
@candidate_skill_routes.route("/candidate_skill/<int:candidate_skill_id>", methods=["PUT"])
def update_candidate_skill(candidate_skill_id):
    data = request.json

    connection = get_connection()
    cursor = connection.cursor()

    query = """
            UPDATE candidate_skill
            SET SKILL_ID = %s
            WHERE ID = %s 
            """

    values = (
        data.get("skill_id"),
        candidate_skill_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Skill updated"})


# DELETE - Delete experience
@candidate_skill_routes.route("/candidate-skills/<int:candidate_skill_id>", methods=["DELETE"])
def delete_candidate_skill(candidate_skill_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
                   DELETE
                   FROM candidate_skill
                   WHERE ID = %s
                   """, (candidate_skill_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Skill deleted"})