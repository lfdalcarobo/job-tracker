from flask import render_template, request, redirect, url_for, flash

from app.routes.candidate_training.candidate_training_routes import candidate_training_routes
from app.repositories.training_type_repository import get_all_training_types
from app.repositories.country_repository import get_all_countries
from app.repositories.candidate_training_repository import (
    get_training_by_id,
    update_training
)


@candidate_training_routes.route(
    "/<int:id>/edit",
    methods=["GET", "POST"]
)
def edit_candidate_training(id):

    training = get_training_by_id(id)

    if not training:
        flash("Training not found.", "error")
        return redirect(url_for("candidate_routes.list_candidates"))

    candidate_id = training["candidate_id"]

    if request.method == "POST":

        update_training(
            training_id=id,
            description=request.form.get("description"),
            training_type_id=request.form.get("training_type_id"),
            country_id=request.form.get("country_id") or None,
            start_date=f"{request.form.get('start_date')}-01" if request.form.get("start_date") else None,
            end_date=f"{request.form.get('end_date')}-01" if request.form.get("end_date") else None
        )

        return redirect(
            url_for(
                "candidate_routes.view_candidate",
                id=candidate_id
            )
        )

    training_types = get_all_training_types()
    countries = get_all_countries()

    return render_template(
        "candidate/training/form.html",
        training=training,
        candidate_id=candidate_id,
        training_types=training_types,
        countries=countries
    )