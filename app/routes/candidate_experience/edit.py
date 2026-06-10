from flask import render_template, request, redirect, url_for, flash
from app.routes.candidate_experience.candidate_experience_routes import candidate_experience_routes
from app.repositories.country_repository import get_all_countries
from app.repositories.type_location_repository import get_all_types_of_locations
from app.repositories.candidate_experience_repository import update_experience
from app.repositories.candidate_experience_repository import get_experience_by_id


@candidate_experience_routes.route(
    "/<int:id>/edit",
    methods=["GET", "POST"]
)
def edit_candidate_experience(id):

    # buscar experiência no banco
    experience = get_experience_by_id(id)

    if not experience:
        flash("Experiência não encontrada.", "error")
        return redirect(url_for("candidate_routes.list_candidates"))

    # 🔥 pega o ID do candidato ANTES do POST/redirect
    candidate_id = experience["CANDIDATE_ID"]

    if request.method == "POST":

        data = {
            "position": request.form.get("position"),
            "enterprise": request.form.get("enterprise"),
            "country_id": request.form.get("country_id"),
            "type_location_id": request.form.get("type_of_location_id"),
            "start_date": f"{request.form.get('start_date')}-01" if request.form.get("start_date") else None,
            "end_date": f"{request.form.get('end_date')}-01" if request.form.get("end_date") else None,
            "description": request.form.get("description")
        }

        update_experience(
            exp_id=id,
            enterprise=request.form.get("enterprise"),
            position=request.form.get("position"),
            country_id=request.form.get("country_id"),
            type_location_id=request.form.get("type_location_id"),
            start_date=f"{request.form.get('start_date')}-01" if request.form.get("start_date") else None,
            end_date=f"{request.form.get('end_date')}-01" if request.form.get("end_date") else None,
            description=request.form.get("description")
        )

        return redirect(url_for(
            "candidate_routes.view_candidate",
            id=candidate_id
        ))

    countries = get_all_countries()
    type_locations = get_all_types_of_locations()

    return render_template(
        "candidate/experience/form.html",
        experience=experience,
        candidate_id=candidate_id,
        countries=countries,
        type_locations=type_locations
    )