from flask import render_template, request, redirect, url_for, flash
from app.routes.candidate_skill.candidate_skill_routes import candidate_skill_routes
from app.repositories.skill_repository import get_all_skills
from app.repositories.candidate_skill_repository import insert_skill


@candidate_skill_routes.route(
    "/candidate/<int:candidate_id>/new",
    methods=["POST"]
)
def create_candidate_skill(candidate_id):
    skill_id = request.form.get("skill_id")

    if skill_id:
        try:
            insert_skill(
                candidate_id=candidate_id,
                skill_id=int(skill_id)
            )
            flash("Skill added successfully!", "success")

        except Exception as e:
            # Verifica se o erro contêm o código 1062 do MySQL ou 'Duplicate entry'
            error_msg = str(e)
            if "1062" in error_msg or "Duplicate" in error_msg:
                flash("This skill has already been added to this candidate.", "warning")
            else:
                flash(f"Error adding skill: {error_msg}", "error")

    return redirect(
        url_for(
            "candidate_routes.view_candidate",
            id=candidate_id,
            _anchor="skills"
        )
    )