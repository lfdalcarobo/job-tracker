from flask import render_template, request, redirect, url_for, flash
from app.routes.candidate_language.candidate_language_routes import candidate_language_routes
from app.repositories.candidate_language_repository import insert_language
from app.repositories.language_repository import get_all_languages
from app.repositories.level_language_repository import get_all_level_languages


@candidate_language_routes.route(
    "/candidate/<int:candidate_id>/new",
    methods=["GET", "POST"]
)
def create_candidate_language(candidate_id):

    if request.method == "POST":
        language_id = request.form.get("language_id")
        level_language_id = request.form.get("level_language_id")

        if language_id and level_language_id:
            # Passa os argumentos individuais esperados pelo repositório
            insert_language(
                candidate_id=candidate_id,
                language_id=int(language_id),
                level_language_id=int(level_language_id)
            )
            flash("Language added successfully!", "success")

        # Redireciona de volta para a view com a âncora #languages
        return redirect(
            url_for(
                "candidate_routes.view_candidate",
                id=candidate_id,
                _anchor="languages"
            )
        )

    # Requisicao GET: Busca as listas para popular os <select> do form
    languages = get_all_languages()
    level_languages = get_all_level_languages()

    return render_template(
        "candidate/language/form.html",
        candidate_id=candidate_id,
        languages=languages,
        level_languages=level_languages
    )