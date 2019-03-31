from flask import Blueprint

apiv2 = Blueprint('apiv2', __name__)

from api.v2.routes import user, mail, groups