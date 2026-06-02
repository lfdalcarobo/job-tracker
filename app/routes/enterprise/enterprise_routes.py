from flask import Blueprint

enterprise_routes = Blueprint("enterprise_routes",__name__,url_prefix="/enterprises")

# importa apenas as rotas (elas devem usar o MESMO blueprint)
from .create import create_enterprise
from .edit import edit_enterprise
from .list import list_enterprises
from .view import get_enterprise_by_id