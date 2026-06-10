from flask import render_template
from app.routes.candidate.candidate_routes import candidate_routes
from app.repositories.candidate_repository import get_candidate_by_id
from app.repositories.candidate_experience_repository import (get_experiences_by_candidate)


@candidate_routes.route("/<int:id>")
def view_candidate(id):

    candidate = get_candidate_by_id(id)

    experiences = get_experiences_by_candidate(id)


    return render_template(
    "candidate/view.html",
    candidate=candidate,
    experiences=experiences
)