from flask import render_template
from app.routes.candidate.candidate_routes import candidate_routes
from app.repositories.candidate_repository import get_candidate_by_id
from app.repositories.candidate_experience_repository import (get_experiences_by_candidate)
from app.repositories.candidate_training_repository import (get_trainings_by_candidate)
from app.repositories.skill_repository import get_all_skills
from app.repositories.candidate_skill_repository import get_skills_by_candidate
from app.repositories.candidate_language_repository import get_languages_by_candidate
from app.repositories.language_repository import get_all_languages
from app.repositories.level_language_repository import get_all_level_languages


@candidate_routes.route("/<int:id>")
def view_candidate(id):

    candidate = get_candidate_by_id(id)

    experiences = get_experiences_by_candidate(id)
    
    trainings = get_trainings_by_candidate(id)

    skills = get_all_skills()

    candidate_skills = get_skills_by_candidate(id)

    languages = get_all_languages()

    level_languages = get_all_level_languages()

    candidate_languages = get_languages_by_candidate(id)


    return render_template(
    "candidate/view.html",
    candidate=candidate,
    experiences=experiences,
    trainings=trainings,
    skills=skills,
    candidate_skills=candidate_skills,
    languages=languages,
    level_languages=level_languages,
    candidate_languages=candidate_languages

)