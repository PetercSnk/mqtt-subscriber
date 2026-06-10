from flask import Flask

from config import Config
from app.extensions import db, bootstrap, csrf, mqtt, scheduler


def createApp():
    """Flask application factory. Creates and configures the flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap.init_app(app)
    csrf.init_app(app)
    mqtt.init_app(app)
    db.init_app(app)
    scheduler.init_app(app)
    scheduler.start()

    from app.subscribe.logging import (
            connectHandler,
            disconnectHandler,
            subscribeHandler,
            unsubscribeHandler
    )
    from app.subscribe.jobs import messageHandler

    from app.models.subscribe import Topic
    from app.subscribe.startup import subscribeToTopic, resetSystems
    with app.app_context():
        db.create_all()
        subscribeToTopic()
        resetSystems()

    from app.subscribe import subscribe
    app.register_blueprint(subscribe)

    from app.errors import errors
    app.register_blueprint(errors)

    return app
