#!/usr/bin/env python3
""" Creating blueprint for API """

from flask import Blueprint

views = Blueprint('views', __name__, url_prefix='/api/v1')
from api.v1.routes.index import *
from api.v1.routes.images import *
from api.v1.routes.users import *