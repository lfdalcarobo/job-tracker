from flask import Blueprint

candidate_training_routes = Blueprint("candidate_training_routes",__name__,url_prefix="/training")


# importa apenas as rotas (elas devem usar o MESMO blueprint)
from .create import create_candidate_training
from .edit import edit_candidate_training
from .delete import delete_candidate_training