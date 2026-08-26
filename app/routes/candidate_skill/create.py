from flask import render_template, request, redirect, url_for
from app.routes.candidate_skill.candidate_skill_routes import candidate_skill_routes
from app.repositories.skill_repository import get_all_skills
from app.repositories.candidate_skill_repository import insert_skill


@candidate_skill_routes.route(
    "/candidate/<int:candidate_id>/new",
    methods=["POST"]
)
def create_candidate_skill(candidate_id):
    skill_id = request.form.get("skill_id")

    if skill_id and skill_id.strip():
        insert_skill(
            candidate_id=candidate_id,
            skill_id=int(skill_id)
        )

    # Adicionado _anchor="skills"
    return redirect(
        url_for(
            "candidate_routes.view_candidate",
            id=candidate_id,
            _anchor="skills"
        )
    )