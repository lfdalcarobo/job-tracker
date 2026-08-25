from flask import render_template, request, redirect, url_for, flash

from app.routes.candidate_skill.candidate_skill_routes import candidate_skill_routes
from app.repositories.skill_repository import get_all_skills
from app.repositories.candidate_skill_repository import (
    get_skill_by_id,
    update_skill
)


@candidate_skill_routes.route(
    "/<int:id>/edit",
    methods=["GET", "POST"]
)
def edit_candidate_skill(id):

    skill = get_skill_by_id(id)

    if not skill:
        flash("Skill not found.", "error")
        return redirect(url_for("candidate_routes.list_candidates"))

    candidate_id = skill["candidate_id"]

    if request.method == "POST":

        update_skill(
            skill_id=id,
            skill_type_id=request.form.get("skill_type_id"),

        )

        return redirect(
            url_for(
                "candidate_routes.view_candidate",
                id=candidate_id
            )
        )

    skill_types = get_all_skill_types()

    return render_template(
        "candidate/skill/form.html",
        skill=skill,
        candidate_id=candidate_id,
        skill_types=skill_types
    )