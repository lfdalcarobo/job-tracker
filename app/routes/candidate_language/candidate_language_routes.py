from flask import Blueprint

candidate_language_routes = Blueprint("candidate_language_routes",__name__,url_prefix="/language")


# importa apenas as rotas (elas devem usar o MESMO blueprint)
from .create import create_candidate_language
from .edit import edit_candidate_language
from .delete import delete_candidate_language