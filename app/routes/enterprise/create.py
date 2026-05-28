from flask import Blueprint, request, redirect, url_for, render_template
from app.repositories.enterprise_repository import create_enterprise_db

enterprise_routes = Blueprint("enterprise_routes", __name__)

# CREATE - create enterprise
@enterprise_routes.route("/create", methods=["GET", "POST"])
def create_enterprise():
    if request.method == "POST":
        name = request.form.get("name")

        create_enterprise_db(name)

        return redirect(url_for("enterprise_routes.create_enterprise"))

    return render_template("enterprise/create.html")