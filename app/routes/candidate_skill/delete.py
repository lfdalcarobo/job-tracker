from flask import redirect, url_for, flash
from app.routes.candidate_skill.candidate_skill_routes import candidate_skill_routes
from app.repositories.candidate_skill_repository import delete_skill


@candidate_skill_routes.route("/candidate/<int:candidate_id>/skill/<int:id>/delete", methods=["POST"])
def delete_candidate_skill(candidate_id, id):

    # Executa a exclusão diretamente no banco de dados
    delete_skill(id)

    flash("Skill successfully removed!", "success")

    
    return redirect(
    url_for(
        "candidate_routes.view_candidate",
        id=candidate_id,
        _anchor="skills"  # Rola a página direto para a seção #skills
    )
)