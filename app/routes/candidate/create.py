from flask import render_template, request, redirect, url_for

from app.routes.candidate.candidate_routes import candidate_routes
from app.repositories.candidate_repository import create_candidate_db
from app.repositories.country_repository import get_all_countries


@candidate_routes.route("/new", methods=["GET", "POST"])
def create_candidate():

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

        new_id = create_candidate_db(
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

        return redirect(url_for("candidate_routes.view_candidate", id=new_id))

    countries = get_all_countries()

    return render_template(
        "candidate/form.html",
        candidate=None,
        countries=countries,
        candidate_id=None

    )