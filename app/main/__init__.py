from flask import Blueprint

main = Blueprint('main', __name__)

# routes
from . import views