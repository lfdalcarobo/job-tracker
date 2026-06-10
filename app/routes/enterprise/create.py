from flask import render_template, request, redirect, url_for

from app.routes.enterprise.enterprise_routes import enterprise_routes
from app.repositories.enterprise_repository import create_enterprise_db


@enterprise_routes.route("/new", methods=["GET", "POST"])
def create_enterprise():

    if request.method == "POST":
        name = request.form["name"]
        situation = "A" if request.form.get("situation") == "A" else "I"

        new_id = create_enterprise_db(name, situation)

        return redirect(url_for(
            "enterprise_routes.view_enterprise",
            id=new_id
        ))

    return render_template("enterprise/form.html", enterprise=None)