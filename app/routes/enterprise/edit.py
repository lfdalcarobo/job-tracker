from flask import render_template, request, redirect, url_for

from app.routes.enterprise.enterprise_routes import enterprise_routes
from app.repositories.enterprise_repository import (
    get_enterprise_by_id,
    update_enterprise_db
)


@enterprise_routes.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_enterprise(id):

    enterprise = get_enterprise_by_id(id)

    next_page = request.args.get("next", "list")

    if request.method == "POST":
        name = request.form["name"]
        situation = request.form["situation"]

        update_enterprise_db(id, name, situation)

        if next_page == "view":
            return redirect(url_for("enterprise_routes.view_enterprise", id=id))
        else:
            return redirect(url_for("enterprise_routes.list_enterprises"))

    return render_template(
        "enterprise/form.html",
        enterprise=enterprise,
        next_page=next_page
    )