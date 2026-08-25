from flask import redirect, url_for, flash

from app.routes.candidate_training.candidate_training_routes import candidate_training_routes

from app.repositories.candidate_training_repository import (
    get_training_by_id,
    delete_training
)


@candidate_training_routes.route("/<int:id>/delete", methods=["POST"])
def delete_candidate_training(id):

    training = get_training_by_id(id)

    if not training:
        flash("Training not found.", "error")
        return redirect(url_for("candidate_routes.list_candidates"))

    candidate_id = training["candidate_id"]

    delete_training(id)

    flash("Training successfully removed!", "success")

    return redirect(
        url_for(
            "candidate_routes.view_candidate",
            id=candidate_id
        )
    )