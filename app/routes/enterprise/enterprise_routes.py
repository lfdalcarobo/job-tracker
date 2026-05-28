from flask import Blueprint

enterprise_routes = Blueprint("enterprise_routes",__name__,url_prefix="/enterprises")

# importa apenas as rotas (elas devem usar o MESMO blueprint)
from .create import create_enterprise
from .update import update_enterprise
from .list import list_enterprises
from .view import view_enterprise