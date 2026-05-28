from flask import Blueprint, render_template
from app.repositories.enterprise_repository import get_all_enterprises

enterprise_routes = Blueprint("enterprise_routes",__name__,url_prefix="/enterprises")

# READ - get all
@enterprise_routes.route("/", methods=["GET"])
def list_enterprises():

    enterprises = get_all_enterprises()

    return render_template("enterprise/list.html",enterprises=enterprises)