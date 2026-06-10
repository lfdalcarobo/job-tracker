from flask import Blueprint

candidate_routes = Blueprint("candidate_routes",__name__,url_prefix="/candidates")

# importa apenas as rotas (elas devem usar o MESMO blueprint)
from .create import create_candidate
from .edit import edit_candidate
from .list import list_candidates
from .view import view_candidate