from flask import render_template, request
from app.repositories.candidate_repository import get_all_candidates
from app.routes.candidate.candidate_routes import candidate_routes


def clean(value):
    return value if value else None


@candidate_routes.route("/list", methods=["GET"])
def list_candidates():

    filters = {
        "name": clean(request.args.get("name")),
        "gender": clean(request.args.get("gender")),
        "email": clean(request.args.get("email")),
        "phone": clean(request.args.get("phone")),
        "date_birth": clean(request.args.get("date_birth"))
    }

    candidates = get_all_candidates(**filters)

    return render_template(
        "candidate/list.html",
        candidates=candidates,
        **filters
    )