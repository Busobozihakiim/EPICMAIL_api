from flask import Blueprint

apiv1 = Blueprint('apiv1', __name__)

from api.v1.routes import user, mail, groups