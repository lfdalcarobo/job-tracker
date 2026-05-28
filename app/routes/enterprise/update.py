from flask import Blueprint, request, redirect, url_for, render_template
from app.repositories.enterprise_repository import update_enterprise_db

enterprise_routes = Blueprint("enterprise_routes", __name__)

# UPDATE - Update enterprise
@enterprise_routes.route("/update/<int:id>", methods=["GET", "POST"])
def update_enterprise(id):
    if request.method == "POST":
        name = request.form.get("name")
        situation = request.form.get("situation")

        update_enterprise_db(id, name, situation)

        return redirect(url_for("enterprise_routes.update_enterprise", id=id))

    return render_template("enterprise/update.html", id=id)