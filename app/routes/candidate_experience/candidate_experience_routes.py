from flask import Blueprint

candidate_experience_routes = Blueprint("candidate_experience_routes",__name__,url_prefix="/experience")


# importa apenas as rotas (elas devem usar o MESMO blueprint)
from .create import create_candidate_experience
from .edit import edit_candidate_experience
from .delete import delete_candidate_experience