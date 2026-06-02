from flask import render_template, request
from app.repositories.enterprise_repository import get_all_enterprises
from app.routes.enterprise.enterprise_routes import enterprise_routes


@enterprise_routes.route("/list", methods=["GET"])
def list_enterprises():

    name = request.args.get("name")

    situation = request.args.get("situation")

    # ✔ DEFAULT AQUI
    if situation is None:
        situation = "A"

    enterprises = get_all_enterprises(name=name, situation=situation)

    return render_template(
        "enterprise/list.html",
        enterprises=enterprises,
        name=name,
        situation=situation
    )