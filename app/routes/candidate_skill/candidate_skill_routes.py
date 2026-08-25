from flask import Blueprint

candidate_skill_routes = Blueprint("candidate_skill_routes",__name__,url_prefix="/skills")


# importa apenas as rotas (elas devem usar o MESMO blueprint)
from .create import create_candidate_skill
from .edit import edit_candidate_skill
from .delete import delete_candidate_skill