from flask import Blueprint

enterprise_routes = Blueprint("enterprise_routes",__name__,url_prefix="/enterprises")

from .create import *
from .update import *
from .list import *
from .view import *