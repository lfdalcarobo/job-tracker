from flask import Blueprint, render_template
from app.repositories.enterprise_repository import get_enterprise_by_id

enterprise_routes = Blueprint("enterprise_routes",__name__,url_prefix="/enterprises")

# READ - view by ID
@enterprise_routes.route("/<int:id>", methods=["GET"])
def view_enterprise(id):
    enterprise = get_enterprise_by_id(id)

    if not enterprise:
        return render_template("errors/404.html"), 404

    return render_template("enterprise/view.html",enterprise=enterprise)