from flask import redirect, url_for, flash

from app.routes.candidate_experience.candidate_experience_routes import candidate_experience_routes

from app.repositories.candidate_experience_repository import (
    get_experience_by_id,
    delete_experience
)


@candidate_experience_routes.route("/<int:id>/delete", methods=["POST"])
def delete_candidate_experience(id):

    experience = get_experience_by_id(id)

    if not experience:
        flash("Experiência não encontrada.", "error")
        return redirect(url_for("candidate.list_candidates"))

    candidate_id = (
        experience.get("candidate_id")
        or experience.get("CANDIDATE_ID")
        or experience.get("candidateId")
    )

    delete_experience(id)

    flash("Experiência removida com sucesso!", "success")

    if not candidate_id:
        return redirect(url_for("candidate.list_candidates"))

    return redirect(url_for(
        "candidate_routes.view_candidate",
        id=candidate_id
    ))