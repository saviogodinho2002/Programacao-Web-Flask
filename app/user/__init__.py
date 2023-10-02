from flask import Blueprint
from werkzeug.urls import url_encode



user = Blueprint('user', __name__, template_folder='templates', static_folder='static')

from . import routes
