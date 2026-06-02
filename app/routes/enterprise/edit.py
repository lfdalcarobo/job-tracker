from flask import Blueprint, request, redirect, url_for, render_template
from app.repositories.enterprise_repository import update_enterprise_db

enterprise_routes = Blueprint("enterprise_routes", __name__)

# UPDATE - Update enterprise
@enterprise_routes.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_enterprise(id):

    enterprise = get_enterprise_by_id(id)

    if request.method == "POST":
        name = request.form["name"]
        situation = request.form["situation"]

        update_enterprise_db(id, name, situation)

        return redirect(url_for(
            "enterprise_routes.get_enterprise_by_id",
            id=id
        ))

    return render_template("enterprise/edit.html", enterprise=enterprise)