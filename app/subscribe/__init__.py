from flask import Blueprint

subscribe = Blueprint("subscribe", __name__)

from app.subscribe import routes
