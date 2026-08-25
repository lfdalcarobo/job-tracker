from flask import render_template, request, redirect, url_for
from app.routes.candidate_skill.candidate_skill_routes import candidate_skill_routes
from app.repositories.skill_repository import get_all_skills
from app.repositories.candidate_skill_repository import insert_skill


@candidate_skill_routes.route(
    "/candidate/<int:candidate_id>/new",
    methods=["GET", "POST"]
)
def create_candidate_skill(candidate_id):

    if request.method == "POST":

        insert_skill(
            candidate_id=candidate_id,
            skill_id=request.form.get("skill_id")
        )

        return redirect(
            url_for(
                "candidate_routes.view_candidate",
                id=candidate_id
            )
        )

    skills = get_all_skills()

    return render_template(
        "candidate/skill/form.html",
        candidate_id=candidate_id,
        skills=skills
    )