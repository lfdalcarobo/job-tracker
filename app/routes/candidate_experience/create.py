from flask import render_template, request, redirect, url_for, flash
from app.routes.candidate_experience.candidate_experience_routes import candidate_experience_routes
from app.repositories.country_repository import get_all_countries
from app.repositories.type_location_repository import get_all_types_of_locations
from app.repositories.candidate_experience_repository import insert_experience


@candidate_experience_routes.route(
    "/candidate/<int:candidate_id>/new",
    methods=["GET", "POST"]
)
def create_candidate_experience(candidate_id):

    if request.method == "POST":

        data = {
            "candidate_id": candidate_id,
            "position": request.form.get("position"),
            "enterprise": request.form.get("enterprise"),
            "country_id": request.form.get("country_id"),
            "type_location_id": request.form.get("type_of_location_id"),
            "start_date": f"{request.form.get('start_date')}-01" if request.form.get("start_date") else None,
            "end_date": f"{request.form.get('end_date')}-01" if request.form.get("end_date") else None,
            "description": request.form.get("description")
        }

        insert_experience(data)


        return redirect(url_for("candidate_routes.view_candidate", id=candidate_id))
    
    countries = get_all_countries()
    type_locations = get_all_types_of_locations()

    return render_template(
        "candidate/experience/form.html",
        candidate_id=candidate_id,
        countries=countries,
        type_locations=type_locations
    )