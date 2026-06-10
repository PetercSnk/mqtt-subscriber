from flask import render_template, current_app

from app.errors import errors


@errors.app_errorhandler(404)
def notFoundError(error):
    current_app.logger.error(error)
    return render_template("errors/404.html"), 404


@errors.app_errorhandler(400)
def badRequestError(error):
    current_app.logger.error(error)
    return render_template("errors/400.html"), 400
