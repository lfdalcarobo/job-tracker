from flask import redirect, url_for, flash
from app.routes.candidate_language.candidate_language_routes import candidate_language_routes
from app.repositories.candidate_language_repository import delete_language


@candidate_language_routes.route("/candidate/<int:candidate_id>/language/<int:id>/delete", methods=["POST"])
def delete_candidate_language(candidate_id, id):

    delete_language(id)

    flash("Idioma removido com sucesso!", "success")

    return redirect(
        url_for(
            "candidate_routes.view_candidate",
            id=candidate_id,
            _anchor="languages"
        )
    )