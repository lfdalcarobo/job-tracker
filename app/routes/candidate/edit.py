from flask import render_template, request, redirect, url_for

from app.routes.candidate.candidate_routes import candidate_routes
from app.repositories.candidate_repository import (
    get_candidate_by_id,
    update_candidate_db
)
from app.repositories.country_repository import get_all_countries


@candidate_routes.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_candidate(id):

    candidate = get_candidate_by_id(id)

    if not candidate:
        return redirect(url_for("candidate_routes.list_candidates"))

    candidate_id = candidate["ID"]

    if request.method == "POST":
        name = request.form["name"]
        date_birth = request.form["date_birth"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        email = request.form["email"]
        address = request.form["address"]
        city = request.form["city"]
        country = request.form["country"] or None
        linkedin = request.form["linkedin"]

        update_candidate_db(
            id,
            name,
            date_birth,
            gender,
            phone,
            email,
            address,
            city,
            country,
            linkedin
        )

        return redirect(url_for("candidate_routes.view_candidate", id=id))

    countries = get_all_countries()

    return render_template(
        "candidate/form.html",
        candidate_id=candidate_id,
        candidate=candidate,
        countries=countries
    )