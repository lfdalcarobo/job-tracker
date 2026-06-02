from flask import render_template
from app.routes.enterprise.enterprise_routes import enterprise_routes
from app.repositories.enterprise_repository import get_enterprise_by_id


@enterprise_routes.route("/<int:id>")
def view_enterprise(id):

    enterprise = get_enterprise_by_id(id)

    return render_template(
        "enterprise/view.html",
        enterprise=enterprise
    )