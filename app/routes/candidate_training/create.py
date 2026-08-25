from flask import render_template, request, redirect, url_for
from app.routes.candidate_training.candidate_training_routes import candidate_training_routes
from app.repositories.training_type_repository import get_all_training_types
from app.repositories.country_repository import get_all_countries
from app.repositories.candidate_training_repository import insert_training


@candidate_training_routes.route(
    "/candidate/<int:candidate_id>/new",
    methods=["GET", "POST"]
)
def create_candidate_training(candidate_id):

    if request.method == "POST":

        insert_training(
            candidate_id=candidate_id,
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
        candidate_id=candidate_id,
        training_types=training_types,
        countries=countries
    )