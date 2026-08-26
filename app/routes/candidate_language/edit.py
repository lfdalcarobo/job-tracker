from flask import render_template, request, redirect, url_for, flash
from app.routes.candidate_language.candidate_language_routes import candidate_language_routes
from app.repositories.candidate_language_repository import (
    get_candidate_language_by_id,
    update_language
)
from app.repositories.language_repository import get_all_languages
from app.repositories.level_language_repository import get_all_level_languages


@candidate_language_routes.route(
    "/<int:id>/edit",
    methods=["GET", "POST"]
)
def edit_candidate_language(id):

    # 1. Buscar o registro de vínculo pelo ID
    language = get_candidate_language_by_id(id)

    if not language:
        flash("Idioma não encontrado.", "error")
        return redirect(url_for("candidate_routes.list_candidates"))

    # 2. Captura tolerante da chave candidate_id
    candidate_id = language.get("candidate_id") or language.get("CANDIDATE_ID")

    if request.method == "POST":
        language_id = request.form.get("language_id")
        level_language_id = request.form.get("level_language_id")

        if language_id and level_language_id:
            # Passa os 4 argumentos exatos definidos na assinatura do repositório
            update_language(
                candidate_language_id=id,
                candidate_id=candidate_id,
                language_id=int(language_id),
                level_language_id=int(level_language_id)
            )
            flash("Idioma atualizado com sucesso!", "success")

        # Redireciona de volta para a view com a âncora #languages
        return redirect(
            url_for(
                "candidate_routes.view_candidate",
                id=candidate_id,
                _anchor="languages"
            )
        )

    # 3. Requisição GET: Busca os domínios para carregar as opções no form
    languages = get_all_languages()
    level_languages = get_all_level_languages()

    return render_template(
        "candidate/language/form.html",
        language=language,
        candidate_id=candidate_id,
        languages=languages,
        level_languages=level_languages
    )