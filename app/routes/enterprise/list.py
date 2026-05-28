from flask import render_template
from app.repositories.enterprise_repository import get_all_enterprises
from app.routes.enterprise.enterprise_routes import enterprise_routes

# READ - get all
@enterprise_routes.route("/list", methods=["GET"])
def list_enterprises():

    enterprises = get_all_enterprises()

    print(enterprises)

    return render_template("enterprise/list.html", enterprises=enterprises)