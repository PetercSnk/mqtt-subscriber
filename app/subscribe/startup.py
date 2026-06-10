from sqlalchemy import select

from app.extensions import mqtt, db
from app.models.subscribe import Topic
from app.subscribe.systems import off


def subscribeToTopic():
    """Subscribes to the topic stored in the database on boot.
    """
    topic = db.session.execute(select(Topic)).scalar_one_or_none()
    if topic is not None:
        mqtt.subscribe(topic.name)


def resetSystems():
    """Turns all systems off on boot.
    """
    off()
